from django.apps import apps
from django.db.models import Model


def get_model(app_label: str, model_name: str) -> Model:
    """
    Get model from app_label and model_name
    """
    return apps.get_model(app_label=app_label, model_name=model_name)
