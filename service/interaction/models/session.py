from django.db import models


class Session(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)

    created = models.DateTimeField(auto_now_add=True)
