from django.db import models
from lib.utils.db.fields import ConstantField
from lib.utils.constant import Constant


class SessionAccess(models.Model):
    class Type(Constant):
        READ = 0
        WRITE = 1

    user_id = models.PositiveIntegerField(db_index=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)

    type_id = ConstantField(Type, default=Type.READ)

    class Meta:
        unique_together = (('user_id', 'type_id', 'session'),)
