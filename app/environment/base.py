import os

SECRET_KEY = os.environ.get('SECRET_KEY', None)
DATABASE_URL = os.environ.get('DATABASE_URL', None)
