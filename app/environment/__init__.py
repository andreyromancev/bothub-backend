import os


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    from environment.production import *
elif ENVIRONMENT == 'staging':
    from environment.staging import *
else:
    from environment.development import *
