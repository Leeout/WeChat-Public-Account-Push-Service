"""
提供新浪网每日科技-手机频道新闻，并推送至公众号
"""
import re
import time
import requests
import threading
from queue import Queue
from bs4 import BeautifulSoup
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file
from utils.time_base import get_today_date

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'pro_setting.ini')

FILE_LOCK = threading.Lock()
SHARE_Q = Queue()  # 构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 2  # 设置线程的个数


class MyThread(threading.Thread):
    """
    抓取线程类，需要继承线程类Thread
    """

    def __init__(self, func):
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.func = func  # 传入线程函数逻辑

    def run(self):
        """
        线程在调用过程中就会调用对应的run方法
        """
        self.func()


def worker():
    """
    队列中获取任务并开始处理新闻信息
    :return:
    """
    global SHARE_Q
    while not SHARE_Q.empty():
        url = SHARE_Q.get()  # 获得任务
        get_news_info(url)
        time.sleep(1)
        SHARE_Q.task_done()


def get_news_info(url):
    """
    :param url: 要爬取的网站地址
    :return: 处理结果
    """
    try:
        req = requests.get(url)
        html = req.text
        div_bf = BeautifulSoup(html, "html.parser")
        content = div_bf.select('.list01_new h3 a')
        logger.info('爬虫爬取内容：%s', content)
        if not content:
            return '爬虫爬取失败，内容为空！'

        get_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
        get_title = r'<a .*?>(.*?)</a>'
        url = re.findall(get_url, str(content), re.I | re.S | re.M)
        title = re.findall(get_title, str(content), re.S | re.M)
        if len(title) != len(url):
            return '新闻数量匹配异常！请检查爬取位置！'

        requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + \
                     '?content=%s 小机为您推送' % get_today_date())
        for i, j in zip(title[:10], url[:10]):  # 遍历两个列表，取前十条数据
            data = '标题：%s\n链接：%s\n' % (i, j)
            time.sleep(1)
            requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + \
                         '?content=' + data)
        return '新闻信息获取成功，并推送完成！'

    except Exception as error:
        requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + \
                     '?content=%s 新闻获取失败，原因：%s', (get_today_date(), error))
        return '获取新闻信息失败，请稍后再试!'


def start_push():
    """
    多线程主要运行函数
    :return:
    """
    global SHARE_Q
    threads = []
    new_url = CFG.get('news_push', 'url')
    SHARE_Q.put(new_url)  # 把URL塞入队列
    for i in range(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()  # 线程开始处理任务
        threads.append(thread)
    for thread in threads:
        thread.join()  # 等待所有线程执行到此处再继续往下执行
    SHARE_Q.join()


if __name__ == '__main__':
    start_push()
