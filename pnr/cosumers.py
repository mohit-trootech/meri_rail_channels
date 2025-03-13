from channels.generic.websocket import SyncConsumer
from json import loads, dumps
from pnr.service import PnrService


class PnrComsumer(SyncConsumer):
    service_class = PnrService

    def websocket_connect(self, event):
        print("connected", event)
        self.send({"type": "websocket.accept"})

    def websocket_receive(self, event):
        try:
            print("received", event)
            data = loads(event["text"])
            dt = self.service_class().use_selenium(data=data["data"])
            print(dt)
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
