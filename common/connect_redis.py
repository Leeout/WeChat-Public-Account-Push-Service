import redis
from configparser import ConfigParser
from common.logger import logger
from common.get_file import get_file

cfg = ConfigParser()
cfg.read(get_file('/config/') + 'pro_setting.ini')


def connect_redis():
    try:
        pool = redis.ConnectionPool(host=cfg.get('redis', 'host'), port=cfg.get('redis', 'port'),
                                    db=cfg.get('redis', 'db'))
        return redis.Redis(connection_pool=pool)
    except Exception as error:
        logger.error("redis连接异常，原因为：", error)
        return
