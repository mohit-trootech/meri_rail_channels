from django_extensions.db.models import TimeStampedModel, ActivatorModel
from django.db.models import CharField, JSONField


class PnrStatus(TimeStampedModel, ActivatorModel):
    pnr = CharField(max_length=10)
    data = JSONField()

    class Meta:
        db_table = "pnr_status"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.pnr
