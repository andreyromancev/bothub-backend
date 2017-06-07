from django.db import models
from model_utils.models import TimeStampedModel


class BotProfile(TimeStampedModel):
    user_id = models.PositiveIntegerField(db_index=True, unique=True)

    name = models.CharField(max_length=32, db_index=True)
    short_description = models.TextField()
    description = models.TextField()
