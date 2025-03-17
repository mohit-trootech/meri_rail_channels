from settings.base import *  # noqa
from settings.base import config

DEBUG = False

ALLOWED_HOSTS = ["*", config.get("ALLOWED_HEADER_IP"), config.get("ALLOWED_HEADER_DNS")]
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}
