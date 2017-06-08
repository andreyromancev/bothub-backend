from django.db import models


class BotAccess(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)
    bot = models.ForeignKey('BotProfile', on_delete=models.CASCADE)

