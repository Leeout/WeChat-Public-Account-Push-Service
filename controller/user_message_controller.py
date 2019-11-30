"""
控制器:获取微信粉丝发送的消息
"""
from flask import request
from flask import Blueprint
from flask import render_template
from utils.get_file import get_file
from configparser import ConfigParser
from services.user_message_service import wechat_push_service

USER_MESSAGE = Blueprint('send_message_to_jige', __name__)
USER_COMMENTS = Blueprint('user_comments', __name__)

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'pro_setting.ini')


@USER_MESSAGE.route('/SendMessageTojige', methods=['get', 'post'])
def send_message_to_jige():
    """
    获取用户通知，限一分钟一次
    :return: 网页展示处理结果
    """
    response = wechat_push_service('short_message', CFG.get('wxpush', 'content'))
    return render_template('send_message.html', message=response) if response == '处理成功' or \
                                                                     '消息发送过于频繁' else render_template(
        'send_message.html', message='通知服务出错，请加机哥微信联系！')


@USER_COMMENTS.route('/SendMessageTojige/UserComments', methods=['post'])
def user_comments():
    """
    获取用户留言，限每天一次
    :return: 网页展示处理结果
    """
    comments = request.form.get('comments')
    response = wechat_push_service('user_comments', comments)
    return render_template('user_comments.html', message=response) if comments != '' else \
        render_template('user_comments.html', message='输入不能为空！')


