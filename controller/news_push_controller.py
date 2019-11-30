"""
控制器:获取新浪网科技-手机类新闻
"""
from flask import Blueprint
from flask import render_template
from configparser import ConfigParser
from services.news_push_service import get_news_info
from utils.get_file import get_file

NEWS_PUSH = Blueprint('news_push', __name__)

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'pro_setting.ini')


@NEWS_PUSH.route('/SendMessageTojige/NewsPush', methods=['get'])
def news_push():
    """
    获取新浪网科技-手机类新闻，并自动推送
    :return: 网页展示处理结果
    """
    message = get_news_info(CFG.get('news_push', 'url'))
    return render_template('user_comments.html', message=message)
