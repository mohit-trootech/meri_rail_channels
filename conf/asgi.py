import os
from dotenv import dotenv_values
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from conf.routing import websocket_urlpatterns

config = dotenv_values(".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
