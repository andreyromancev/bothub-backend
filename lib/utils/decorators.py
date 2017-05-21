from django.conf import settings
from functools import wraps


def pass_for_development(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        if settings.IS_DEVELOPMENT:
            return
        else:
            return function(*args, **kwargs)
    return wrap
