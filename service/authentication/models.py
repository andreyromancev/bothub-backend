import hashlib
import random
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from model_utils import Choices

from lib.utils.mailer import mail_users

__all__ = []


class User(AbstractUser):
    TYPE = Choices(
        (0, 'user', 'user'),
        (1, 'bot', 'bot'),
    )

    type_id = models.PositiveIntegerField(choices=TYPE, default=TYPE.user)

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
