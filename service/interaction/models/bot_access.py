from django.db import models


class BotAccess(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)
    bot_id = models.PositiveIntegerField(db_index=True)
