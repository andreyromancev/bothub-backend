import hashlib
import random

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from bothub.utils.mailer import mail_users

__all__ = []


def _prepare_for_activation(self):
    salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
    activation_key = hashlib.sha1((salt + self.username).encode('utf-8')).hexdigest()

    self.email = self.username
    self.is_active = False
    self.password = activation_key
    self.save()

    mail_users([self.email], 'email_confirm', context={
        'activation_url': '{}/user_activate/?activation_key={}'.format(settings.SITE_WEB, activation_key)
    })


def _activate(self, password):
    self.is_active = True
    self.password = make_password(password)
    self.save()


User.add_to_class('prepare_for_activation', _prepare_for_activation)
User.add_to_class('activate', _activate)
