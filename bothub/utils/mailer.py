import os

from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings
from celery import shared_task
from smtplib import SMTPException

from .decorators import pass_for_development


def mail_manager(template_path, context=None):
    _send_mail.delay([settings.MAILER_MANAGER_EMAIL], template_path, context)


def mail_admin(template_path, context=None):
    _send_mail.delay([settings.MAILER_ADMIN_EMAIL], template_path, context)


def mail_users(email_list, template_path, context=None):
    _send_mail.delay(email_list, template_path, context)


@shared_task(autoretry_for=(SMTPException,), retry_kwargs={'max_retries': 3})
@pass_for_development
def _send_mail(email_list, template_path, context=None):
    message = EmailMessage(
        subject=loader.get_template(os.path.join('mail', template_path, 'subject.html')).render(context),
        body=loader.get_template(os.path.join('mail', template_path, 'message.html')).render(context),
        from_email=settings.MAILER_FROM_EMAIL,
        to=email_list,
    )
    message.content_subtype = 'html'
    message.send()
