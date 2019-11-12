import requests
from config.setting import WXPUSH


def wx_message_push():
    response = requests.get(WXPUSH['open_api'] + WXPUSH['content'])
    return response.json()['msg']
