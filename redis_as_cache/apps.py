from django.apps import AppConfig


class RedisAsCacheConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'redis_as_cache'
