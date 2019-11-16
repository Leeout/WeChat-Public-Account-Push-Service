from flask import request
from common.connect_redis import connect_redis


def get_api_request_count(redis_key, expired_time):
    redis = connect_redis()
    user_ip = request.remote_addr
    key = user_ip + redis_key
    limit = 1  # limit表示限制访问次数
    expired_time = expired_time  # expired_time表示key的过期时间为60秒
    is_excced = 0  # is_excced表示key是否过期: 0不过期 1过期
    if redis.exists(key):
        redis.incr(key)
        count = int(redis.get(key))
        if count > limit:
            is_excced = 1
    else:
        redis.set(key, 1)
        redis.expire(key, expired_time)
    return is_excced
