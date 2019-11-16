from flask import request
from flask import Blueprint
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from configparser import ConfigParser
from services.wechat_push_service import wechat_push_service
from common.get_file import get_file

send_to_jige = Blueprint('send_message_to_jige', __name__)
send_comments_to_jige = Blueprint('user_comments', __name__)

cfg = ConfigParser()
cfg.read(get_file('/config/') + 'dev_setting.ini')


class WebFormCheck(FlaskForm):
    textarea = TextAreaField(validators=[DataRequired('输入不能为空哦！')])
    submit = SubmitField()


@send_to_jige.route('/SendMessageTojige', methods=['get', 'post'])
def send_message_to_jige():
    try:
        response = wechat_push_service('short_message', cfg.get('wxpush', 'content'))
        if response == '处理成功' or '消息发送过于频繁':
            form = WebFormCheck()
            if form.validate_on_submit():
                comments = form.textarea.data
            return render_template('send_message.html', message=response, form=form)
        else:
            return render_template('send_message.html', message='通知服务出错，请加机哥微信联系！')
    except Exception as error:
        print("服务异常，原因为：", error)
        return render_template('send_message.html', message='服务器异常，消息发送失败，请加机哥微信联系！')


@send_comments_to_jige.route('/SendMessageTojige/UserComments', methods=['post'])
def user_comments():
    comments = request.form.get('comments')
    print(comments)
    response = wechat_push_service('user_comments', comments)
    return render_template('user_comments.html', message=response)
