from settings.base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "192.168.0.17", "localhost"]
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}
