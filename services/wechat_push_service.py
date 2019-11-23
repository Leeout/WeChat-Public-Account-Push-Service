import requests
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file
from utils.get_api_request_count import get_api_request_count

cfg = ConfigParser()
cfg.read(get_file('/config/') + 'pro_setting.ini')


def wechat_push_service(func_name, user_message):
    if func_name == 'short_message':
        if get_api_request_count(':send_message_jige', 300) == 0:
            response = requests.get(cfg.get('wxpush', 'open_api') + cfg.get('wxpush', 'uid') + user_message)
            logger.info('微信通知服务返回：%s', response.text)
            return response.json()['msg']
        else:
            return "消息发送过于频繁!"
    else:
        if get_api_request_count(':user_comments', 86400) == 0:
            response = requests.get(
                cfg.get('wxpush', 'open_api') + cfg.get('wxpush', 'uid') + '?content=' + user_message)
            logger.info('微信通知服务返回：%s', response.text)
            return response.json()['msg']
        else:
            return "留言已经发送过啦!"
