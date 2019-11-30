import requests
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'dev_setting.ini')


def lagou_jd_push_service():
    index_url = CFG.get('lagou', 'index_url')
    url = CFG.get('lagou', 'search_api')
    jd_hyper_links = CFG.get('lagou', 'jd_hyper_links')

    headers = {
        'Accept': CFG.get('browser_headers', 'Accept'),
        'Referer': CFG.get('lagou', 'Referer'),
        'User-Agent': CFG.get('browser_headers', 'User-Agent'),
        'Host': CFG.get('lagou', 'Host')
    }
    data = {
        'first': 'false',
        'pn': 1,
        'kd': CFG.get('lagou', 'kd')
    }
    s = requests.Session()  # 建立session
    cookie = s.get(url=index_url, headers=headers, timeout=3).cookies  # 获取cookie
    response = s.post(url=url, headers=headers, data=data, cookies=cookie, timeout=3)
    show_id = response.json()['content']['showId']
    company_info = response.json()['content']['positionResult']['result']
    logger.info(company_info)

    for i in range(10):
        key = company_info[i]
        data = '公司名:%s(%s)\n薪资范围:%s\nJD链接:%s' % (
            key['companyFullName'], key['financeStage'], key['salary'], jd_hyper_links % (key['positionId'], show_id))
        requests.get(CFG.get('wxpush', 'open_api') + CFG.get('wxpush', 'uid') + '?content=' + data)
    return '拉钩JD爬取成功，并推送完成！'


if __name__ == '__main__':
    lagou_jd_push_service()
