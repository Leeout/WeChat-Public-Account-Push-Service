import re
import time
import requests
import threading
from queue import Queue
from bs4 import BeautifulSoup
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file

cfg = ConfigParser()
cfg.read(get_file('/config/') + 'dev_setting.ini')

FILE_LOCK = threading.Lock()
SHARE_Q = Queue()  # 构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 2  # 设置线程的个数


class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.func = func  # 传入线程函数逻辑

    def run(self):
        self.func()


def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        url = SHARE_Q.get()  # 获得任务
        get_news_info(url)
        time.sleep(1)
        SHARE_Q.task_done()


def get_news_info(url):
    try:
        req = requests.get(url)
        html = req.text.encode('ISO 8859-1')
        div_bf = BeautifulSoup(html, "html.parser")
        div = div_bf.find_all('ul', class_="seo_data_list")

        get_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
        get_title = r'<a .*?>(.*?)</a>'
        news_url = re.findall(get_url, str(div), re.I | re.S | re.M)
        news_title = re.findall(get_title, str(div), re.S | re.M)
        logger.debug('新闻总数：%s个，链接总数：%s个 \n' % (len(news_title), len(news_url)))

        for i, j in zip(news_title[:10], news_url[:10]):  # 对两个列表遍历
            data = '小机今日推送\n标题：%s\n链接：%s\n' % (i, j)
            response = requests.get(cfg.get('wxpush', 'open_api') + cfg.get('wxpush', 'uid') + '?content=' + data)
            time.sleep(1)
            logger.debug('微信推送API Response:', response.json())
        return '新闻信息获取成功，并推送完成！'

    except Exception as error:
        logger.error('获取失败，原因：%s', error)
        return '获取新闻信息失败，请稍后再试!'


def start_push():
    global SHARE_Q
    threads = []
    new_url = cfg.get('news_push', 'url')
    for index in range(10):
        SHARE_Q.put(new_url)  # 把URL塞入队列
    for i in range(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()  # 线程开始处理任务
        threads.append(thread)
    for thread in threads:
        thread.join()
    SHARE_Q.join()


if __name__ == '__main__':
    start_push()
