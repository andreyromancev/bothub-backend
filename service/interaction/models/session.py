from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Session(TimeStampedModel):
    user_id = models.PositiveIntegerField(db_index=True)


class SessionAccess(models.Model):
    TYPES = Choices(
        (0, 'read'),
        (1, 'write'))

    user_id = models.PositiveIntegerField(db_index=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    type = models.PositiveIntegerField(choices=TYPES)

    class Meta:
        unique_together = (('user_id', 'type', 'session'),)
