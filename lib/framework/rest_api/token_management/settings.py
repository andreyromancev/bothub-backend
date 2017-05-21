from django.conf import settings

TOKEN_DEFAULT_SERVICE = getattr(settings, 'TOKEN_DEFAULT_SERVICE', 'service')
