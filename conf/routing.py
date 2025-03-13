from django.urls import path
from pnr.cosumers import PnrComsumer

websocket_urlpatterns = [
    path("ws/pnr/", PnrComsumer.as_asgi()),
]
