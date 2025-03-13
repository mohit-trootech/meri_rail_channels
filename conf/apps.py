from django.apps import AppConfig
from utils.selenium_service import SeleniumService


class ConfConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "conf"

    def ready(self):
        SeleniumService()
