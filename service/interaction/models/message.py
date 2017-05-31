from django.db import models
from model_utils.models import TimeStampedModel


class Message(TimeStampedModel):
    user_id = models.PositiveIntegerField(db_index=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    text = models.TextField()
