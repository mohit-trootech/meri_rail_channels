import os
from dotenv import dotenv_values
from django.core.wsgi import get_wsgi_application

config = dotenv_values(".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", config.get("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()
