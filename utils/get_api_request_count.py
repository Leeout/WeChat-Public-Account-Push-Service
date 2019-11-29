"""
查询接口请求次数的服务
"""
from flask import request
from utils.logger import logger
from utils.connect_redis import connect_redis


def get_api_request_count(redis_key, key_expired_time):
    """
    查询接口请求次数
    :param redis_key: 查询的redis key
    :param expired_time: redis key的有效时间
    :return:
    """
    redis = connect_redis()
    user_ip = request.remote_addr
    key = user_ip + redis_key
    limit = 1  # limit表示限制访问次数
    expired_time = key_expired_time  # expired_time表示key的过期时间
    is_excced = 0  # is_excced表示key是否过期: 0不过期 1过期
    if redis.exists(key):
        redis.incr(key)
        logger.debug('redis key:%s,value +1', key)
        count = int(redis.get(key))
        if count > limit:
            is_excced = 1
    else:
        redis.set(key, 1)
        redis.expire(key, expired_time)
        logger.debug('redis key:%s 设置成功，value为1，过期时间为:%s', key, expired_time)
    return is_excced
