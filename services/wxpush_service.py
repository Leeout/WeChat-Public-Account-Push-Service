import os
import requests
from configparser import ConfigParser
from common.api_request_count_check import api_request_count_check

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/config/'
cfg = ConfigParser()
cfg.read(root_path + 'setting.ini')


def wx_message_push():
    if api_request_count_check() == 0:
        response = requests.get(cfg.get('wxpush', 'open_api') + cfg.get('wxpush', 'content'))
        return response.json()['msg']
    else:
        return '消息发送过于频繁'
