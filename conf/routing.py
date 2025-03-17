from django.urls import path
from pnr.cosumers import PnrConsumer
from seat.cosumers import SeatConsumer
from fare.cosumers import FareConsumer

websocket_urlpatterns = [
    path("ws/pnr/", PnrConsumer.as_asgi()),
    path("ws/seat/", SeatConsumer.as_asgi()),
    path("ws/fare/", FareConsumer.as_asgi()),
]
