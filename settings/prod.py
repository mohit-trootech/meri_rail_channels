from settings.base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ["*", "65.2.176.206"]
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}
