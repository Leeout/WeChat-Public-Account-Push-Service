"""
提供拉钩每日测试开发岗位的JD，并推送至公众号
"""
import requests
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'dev_setting.ini')


def lagou_jd_push_service(page, number):
    """
    拉钩每日测试开发岗位的JD
    :param page: 获取的页数
    :param number: 获取的条数
    :return: 网页展示处理后的消息
    """
    index_url = CFG.get('lagou', 'index_url')
    search_api = CFG.get('lagou', 'search_api')
    jd_link = CFG.get('lagou', 'jd_hyper_links')
    headers = {
        'Accept': CFG.get('browser_headers', 'Accept'),
        'Referer': CFG.get('lagou', 'Referer'),
        'User-Agent': CFG.get('browser_headers', 'User-Agent'),
        'Host': CFG.get('lagou', 'Host')
    }
    post_data = {
        'first': 'false',
        'pn': page,
        'kd': CFG.get('lagou', 'kd')
    }
    session = requests.Session()  # 建立session
    cookie = session.get(url=index_url, headers=headers, timeout=3).cookies  # 获取cookie
    response = session.post(url=search_api, headers=headers, data=post_data, cookies=cookie, timeout=3)

    show_id = response.json()['content']['showId']
    company_info = response.json()['content']['positionResult']['result']
    logger.debug(company_info)

    for i in range(number):
        key = company_info[i]
        data = '公司名:%s(%s)\n薪资范围:%s\nJD链接:%s' % (key['companyFullName'],
                                                 key['financeStage'], key['salary'],
                                                 jd_link % (key['positionId'], show_id))
        requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + '?content=' + data)
    return '拉钩JD爬取成功，并推送完成！'


if __name__ == '__main__':
    lagou_jd_push_service(1, 10)
