"""
API入口文件
"""
from flask import Flask
from controller.user_message_controller import USER_MESSAGE
from controller.user_message_controller import USER_COMMENTS
from controller.news_push_controller import NEWS_PUSH
from controller.lagou_jd_controller import LAGOU_JD

APP = Flask(__name__)

APP.register_blueprint(USER_MESSAGE)
APP.register_blueprint(USER_COMMENTS)
APP.register_blueprint(NEWS_PUSH)
APP.register_blueprint(LAGOU_JD)

@APP.route('/')
def index():
    """
    入口
    """
    return '欢迎来到机哥的世界！'


if __name__ == '__main__':
    APP.run(debug=True)
