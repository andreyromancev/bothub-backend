from django.conf import settings


def pass_for_development(function):
    def wrap(*args, **kwargs):
        if settings.IS_DEVELOPMENT:
            return
        else:
            return function(*args, **kwargs)
    return wrap
