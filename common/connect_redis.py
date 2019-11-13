import os
import redis
from configparser import ConfigParser

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/config/'
cfg = ConfigParser()
cfg.read(root_path + 'setting.ini')


def connect_redis():
    try:
        pool = redis.ConnectionPool(host=cfg.get('redis', 'host'), port=cfg.get('redis', 'port'),
                                    db=cfg.get('redis', 'db'))
        return redis.Redis(connection_pool=pool)
    except Exception as error:
        print("redis连接异常，原因为：", error)
        return
