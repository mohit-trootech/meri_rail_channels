from django_extensions.db.models import TimeStampedModel, ActivatorModel
from utils.model import BaseModel


class SeatStatus(BaseModel, TimeStampedModel, ActivatorModel):
    class Meta:
        db_table = "seat_status"
        ordering = ["-created"]
