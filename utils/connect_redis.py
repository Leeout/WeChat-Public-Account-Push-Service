"""
连接redis服务
"""
import redis
from configparser import ConfigParser
from utils.logger import logger
from utils.get_file import get_file

CFG = ConfigParser()
CFG.read(get_file('/config/') + 'pro_setting.ini')


def connect_redis():
    """
    连接redis
    :return: 开启连接通道
    """
    try:
        pool = redis.ConnectionPool(host=CFG.get('redis', 'host'), port=CFG.get('redis', 'port'),
                                    db=CFG.get('redis', 'db'))
        return redis.Redis(connection_pool=pool)
    except Exception as error:
        logger.error("redis连接异常，原因为：%s", error)
