import os

from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings



def mail_manager(template_path, context=None):
    send_mail([settings.MAILER_MANAGER_EMAIL], template_path, context)


def mail_admin(template_path, context=None):
    send_mail([settings.MAILER_ADMIN_EMAIL], template_path, context)


def send_mail(email_list, template_path, context=None):
    message = EmailMessage(
        subject=loader.get_template(os.path.join('mail', template_path, 'subject.html')).render(context),
        body=loader.get_template(os.path.join('mail', template_path, 'message.html')).render(context),
        from_email=settings.MAILER_FROM_EMAIL,
        to=email_list,
    )
    message.content_subtype = 'html'
    message.send()

