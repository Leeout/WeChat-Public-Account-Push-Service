from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/SendMessageTojige', methods=['get', 'post'])
def send_message():
    try:
        wxpusher_api = "http://wxpusher.zjiecode.com/demo/send/custom/UID_zHxE57xTgyvksbJ4C9CQLa29dAPY?content="
        content = "有粉丝发送了消息，请登录查看订阅号!"
        response = requests.get(wxpusher_api + content)
        if response.json()['msg'] == '处理成功':
            return render_template('send_message.html', message="通知机哥成功！")
        else:
            return render_template('send_message.html', message="通知服务出错，请加机哥微信联系！")
    except Exception as error:
        print("服务异常，原因为：%s", error)
        return render_template('send_message.html', message="服务器异常，消息发送失败，请加机哥微信联系！")


if __name__ == '__main__':
    app.run(debug=True)
