from django.db import models
from lib.utils.db.fields import ConstantField
from lib.utils.constant import Constant


class Session(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)

    created = models.DateTimeField(auto_now_add=True)


class SessionAccess(models.Model):
    TYPE = Constant(
        read=0,
        write=1,
    )

    user_id = models.PositiveIntegerField(db_index=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    type_id = ConstantField(TYPE, default=TYPE.read)

    class Meta:
        unique_together = (('user_id', 'type_id', 'session'),)
