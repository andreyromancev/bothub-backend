import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'development_key')
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://bothub:123456@localhost/bothub_db')
