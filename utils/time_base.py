"""
查询时间的服务
"""
import time
import datetime


def get_current_time():
    """获取当前时间点 年-月-日 时:分:秒 格式"""
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_current_hour_minute():
    """获取当前时间，格式为时:分，如 19:36"""
    now_time = datetime.datetime.now()
    return str(now_time.hour) + ':' + str(now_time.minute)


def get_today_date():
    """获取今天日期 年-月-日 格式"""
    return str(datetime.date.today())


if __name__ == '__main__':
    get_today_date()
