"""
控制器:获取拉勾网测试岗位JD
"""
from flask import Blueprint
from flask import render_template
from configparser import ConfigParser
from services.lagou_jd_service import lagou_jd_push_service
from utils.get_file import get_file

LAGOU_JD = Blueprint('lagou_jd_push', __name__)

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'pro_setting.ini')


@LAGOU_JD.route('/SendMessageTojige/LaGouJD', methods=['get'])
def lagou_jd_push():
    """
    获取拉勾网测试岗位JD，并自动推送
    :return: 网页展示处理结果
    """
    message = lagou_jd_push_service()
    return render_template('user_comments.html', message=message)
