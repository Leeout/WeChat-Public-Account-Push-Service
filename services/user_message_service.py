"""
提供微信消息通知的服务
"""
import requests
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file
from utils.get_api_request_count import get_api_request_count

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'pro_setting.ini')


def wechat_push_service(func_name, user_message):
    """
    处理用户发来的消息
    :param func_name: 代表是哪个controller发来的
    :param user_message: 用户的消息
    :return: 网页展示处理后的消息
    """
    if func_name == 'short_message':
        response = requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + \
                                user_message)
        logger.info('微信通知服务返回：%s', response.text)
        return response.json()['msg'] if get_api_request_count(':send_message_jige', 300) == 0 \
            else "消息发送过于频繁!"
    else:
        response = requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + \
                                '?content=' + user_message)
        logger.info('微信通知服务返回：%s', response.text)
        return response.json()['msg'] if get_api_request_count(':user_comments', 86400) == 0 \
            else "留言已经发送过啦!"
