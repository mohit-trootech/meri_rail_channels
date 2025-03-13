from django.apps import apps
from django.db.models import Model
from logging import getLogger


def log_errors(name: str, message: str):
    logger = getLogger(name)
    logger.error(message)


def get_model(app_label: str, model_name: str) -> Model:
    """
    Get model from app_label and model_name
    """
    return apps.get_model(app_label=app_label, model_name=model_name)
