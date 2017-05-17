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


def _activate(self, password):
    assert not self.is_active

    self.is_active = True
    self.password = make_password(password)
    self.save()


def _send_confirmation_email(self):
    assert not self.is_active

    mail_users([self.email], 'email_confirm', context={
        'activation_url': '{}/user_activate/?activation_key={}'.format(settings.SITE_WEB, self.password)
    })


User.add_to_class('prepare_for_activation', _prepare_for_activation)
User.add_to_class('send_confirmation_email', _send_confirmation_email)
User.add_to_class('activate', _activate)
