from django.db.models import JSONField, Model


class BaseModel(Model):
    request_body = JSONField(blank=True, null=True)
    response_body = JSONField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.request_body)
