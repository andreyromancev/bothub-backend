import dj_database_url
from app.environment.base import *


DEBUG = False
ALLOWED_HOSTS = ['stage-api-bothub.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}
