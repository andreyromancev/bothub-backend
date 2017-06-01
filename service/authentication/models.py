import hashlib
import random
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

from lib.utils.mailer import mail_users
from lib.utils.constant import Constant
from lib.utils.db.fields import ConstantField

__all__ = []


class User(AbstractUser):
    TYPE = Constant(
        user=0,
        bot=1,
    )

    type_id = ConstantField(TYPE, default=TYPE.user)

    def prepare_for_activation(self):
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1((salt + self.username).encode('utf-8')).hexdigest()

        self.is_active = False
        self.password = activation_key
        self.save()

    def activate(self, password):
        assert not self.is_active

        self.is_active = True
        self.password = make_password(password)
        self.save()

    def send_confirmation_email(self):
        assert not self.is_active

        mail_users([self.email], 'email_confirm', context={
            'activation_url': '{}/user_activate/?activation_key={}'.format(settings.SITE_WEB, self.password)
        })
