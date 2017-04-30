import os
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY', 'development_key')
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://bothub:123456@localhost/bothub_db')

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}
