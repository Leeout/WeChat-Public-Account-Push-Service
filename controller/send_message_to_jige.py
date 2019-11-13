from flask import Blueprint
from flask import render_template
from services.wxpush_service import wx_message_push

send_to_jige = Blueprint('send_message_to_jige', __name__)


@send_to_jige.route('/SendMessageTojige', methods=['get', 'post'])
def send_message_to_jige():
    try:
        if wx_message_push() == '处理成功':
            return render_template('send_message.html', message='通知机哥成功！')
        elif wx_message_push() == '消息发送过于频繁':
            return render_template('send_message.html', message='呼叫机哥过于频繁，请稍后再试！')
        else:
            return render_template('send_message.html', message='通知服务出错，请加机哥微信联系！')
    except Exception as error:
        print("服务异常，原因为：", error)
        return render_template('send_message.html', message='服务器异常，消息发送失败，请加机哥微信联系！')
