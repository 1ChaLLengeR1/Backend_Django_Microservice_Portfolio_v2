import redis
import pickle
from api.worker.consumer.utils.env import get_env_variable

REDIS_PASSWORD = get_env_variable("REDIS_PASSWORD", default=None)
redis_client = redis.Redis(
    host=get_env_variable("REDIS_HOST"),
    port=int(get_env_variable("REDIS_PORT", default="6379")),
    password=REDIS_PASSWORD if REDIS_PASSWORD else None,
    db=0
)


def get_cache(key):
    cached_data = redis_client.get(key)
    if not cached_data:
        return None
    return pickle.loads(cached_data)


def set_cache_data(key, value, timeout=300, CACHING_ENABLED=True):
    if not CACHING_ENABLED:
        return None

    serialized_value = pickle.dumps(value)
    redis_client.set(key, serialized_value, ex=timeout)


def delete_cache_by_prefix(prefix):
    cursor = 0
    while True:
        cursor, keys = redis_client.scan(cursor, match=f"{prefix}*")
        if keys:
            redis_client.delete(*keys)
        if cursor == 0:
            break


def delete_cache_key(key):
    redis_client.delete(key)
