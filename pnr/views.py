import websockets
import json
from django.views.generic import FormView
from django.forms import Form, CharField
from django.contrib.messages import info


class TestForm(Form):
    message = CharField(max_length=100)


class ProcessDataView(FormView):
    template_name = "base.html"
    form_class = TestForm
    success_url = "/process_data/"

    def form_valid(self, form):
        # Convert async function to sync context
        self.process_data(form.cleaned_data)
        return super().form_valid(form)

    def process_data(self, data):
        """Async WebSocket processing"""
        with websockets.connect("ws://127.0.0.1:8001/ws/process/") as ws:
            ws.send(json.dumps(data))
            response = ws.recv()
            # Handle response
            self.request.session["ws_response"] = json.loads(response)
            info(self.request, "Hello world")
