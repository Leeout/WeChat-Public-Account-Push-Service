"""
API入口文件
"""
from flask import Flask
from controller.wechat_push_controller import USER_MESSAGE
from controller.wechat_push_controller import USER_COMMENTS
from controller.wechat_push_controller import NEWS_PUSH

APP = Flask(__name__)

APP.register_blueprint(USER_MESSAGE)
APP.register_blueprint(USER_COMMENTS)
APP.register_blueprint(NEWS_PUSH)


@APP.route('/')
def index():
    """
    入口
    """
    return '欢迎来到机哥的世界！'


if __name__ == '__main__':
    APP.run(debug=True)
