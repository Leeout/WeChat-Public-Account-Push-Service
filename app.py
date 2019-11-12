from flask import Flask
from controller.send_message_to_jige import send_to_jige

app = Flask(__name__)

app.register_blueprint(send_to_jige)


@app.route('/')
def index():
    return '欢迎来到机哥的世界！'


if __name__ == '__main__':
    app.run(debug=True)
