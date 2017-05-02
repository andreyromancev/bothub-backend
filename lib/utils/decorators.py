from django.conf import settings


def pass_for_development(function):
    def wrap(*args, **kwargs):
        if settings.ENVIRONMENT == 'development':
            return
        else:
            return function(*args, **kwargs)
    return wrap
