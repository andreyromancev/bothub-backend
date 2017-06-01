from django.db import models


class Message(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

