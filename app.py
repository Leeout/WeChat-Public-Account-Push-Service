from flask import Flask
from controller.wechat_push_controller import send_to_jige
from controller.wechat_push_controller import send_comments_to_jige

app = Flask(__name__)

app.register_blueprint(send_to_jige)
app.register_blueprint(send_comments_to_jige)
app.config['SECRET_KEY'] = 'wechat-api-project'


@app.route('/')
def index():
    return '欢迎来到机哥的世界！'


if __name__ == '__main__':
    app.run(debug=True)
