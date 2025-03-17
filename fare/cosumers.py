from channels.generic.websocket import SyncConsumer
from json import loads, dumps
from fare.service import FareService


class FareConsumer(SyncConsumer):
    service_class = FareService()

    def websocket_connect(self, event):
        print("connected", event)
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        try:
            print("received", event)
            data = loads(event["text"])
            dt = self.service_class.use_selenium(data=data["data"])
            self.send({"type": "websocket.send", "text": dumps(dt)})
        except Exception as err:
            self.send(
                {
                    "type": "websocket.send",
                    "text": dumps(str(err)),
                }
            )

    def websocket_disconnect(self, event):
        print("disconnected", event)
