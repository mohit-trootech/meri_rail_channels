from django_extensions.db.models import TimeStampedModel, ActivatorModel
from utils.model import BaseModel


class FareStatus(BaseModel, TimeStampedModel, ActivatorModel):
    class Meta:
        db_table = "fare_status"
        ordering = ["-created"]
