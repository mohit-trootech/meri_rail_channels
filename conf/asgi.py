import os
from dotenv import dotenv_values
from django.core.asgi import get_asgi_application

config = dotenv_values(".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", config.get("DJANGO_SETTINGS_MODULE"))

application = get_asgi_application()
