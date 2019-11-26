from flask import request
from flask import Blueprint
from flask import render_template
from configparser import ConfigParser
from utils.get_file import get_file
from services.wechat_push_service import wechat_push_service
from services.crawling_news_service import get_news_info

send_to_jige = Blueprint('send_message_to_jige', __name__)
send_comments_to_jige = Blueprint('user_comments', __name__)
everyday_news_push = Blueprint('news_push', __name__)

cfg = ConfigParser()
cfg.read(get_file('/config/') + 'pro_setting.ini')


@send_to_jige.route('/SendMessageTojige', methods=['get', 'post'])
def send_message_to_jige():
    response = wechat_push_service('short_message', cfg.get('wxpush', 'content'))
    if response == '处理成功' or '消息发送过于频繁':
        return render_template('send_message.html', message=response)
    else:
        return render_template('send_message.html', message='通知服务出错，请加机哥微信联系！')


@send_comments_to_jige.route('/SendMessageTojige/UserComments', methods=['post'])
def user_comments():
    comments = request.form.get('comments')
    if comments != '':
        response = wechat_push_service('user_comments', comments)
        return render_template('user_comments.html', message=response)
    else:
        return render_template('user_comments.html', message='输入不能为空！')


@everyday_news_push.route('/SendMessageTojige/NewsPush', methods=['get'])
def news_push():
    message = get_news_info(cfg.get('news_push', 'url'))
    return render_template('user_comments.html', message=message)
