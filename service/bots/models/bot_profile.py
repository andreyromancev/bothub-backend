from django.db import models


class BotProfile(models.Model):
    user_id = models.PositiveIntegerField(db_index=True, unique=True)

    name = models.CharField(max_length=32, db_index=True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
