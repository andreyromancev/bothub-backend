import os


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    from app.environment.production import *
elif ENVIRONMENT == 'staging':
    from app.environment.staging import *
else:
    from app.environment.development import *
