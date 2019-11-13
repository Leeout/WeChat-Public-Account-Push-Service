from flask import request
from common.connect_redis import connect_redis


def api_request_count_check():
    redis = connect_redis()
    user_ip = request.remote_addr
    redis_key = user_ip + ':api_count'
    limit = 1  # limit表示限制访问次数
    expired_time = 60  # expired_time表示key的过期时间为60秒
    is_excced = 0  # is_excced表示key是否过期: 0不过期 1过期
    if redis.exists(redis_key):
        redis.incr(redis_key)
        count = int(redis.get(redis_key))
        if count > limit:
            is_excced = 1
    else:
        redis.set(redis_key, 1)
        redis.expire(redis_key, expired_time)
    return is_excced
