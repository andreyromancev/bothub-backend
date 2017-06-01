from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Session(TimeStampedModel):
    user_id = models.PositiveIntegerField(db_index=True)


class SessionAccess(models.Model):
    TYPE = Choices(
        (0, 'read', 'read'),
        (1, 'write', 'write'),
    )

    user_id = models.PositiveIntegerField(db_index=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    type_id = models.PositiveIntegerField(choices=TYPE, default=TYPE.read)

    class Meta:
        unique_together = (('user_id', 'type_id', 'session'),)
