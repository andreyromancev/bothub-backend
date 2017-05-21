import os
import dj_database_url
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = os.environ.get('SECRET_KEY')

IS_PRODUCTION = True

DEBUG = False
ALLOWED_HOSTS = ['api-bothub.herokuapp.com']
SITE_WEB = 'https://web-bothub.herokuapp.com'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'lib.utils.mailer',
    'lib.framework.celeryapp',
    'lib.framework.rest_api.token_management',
    'service.auth_bothub',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://bothub:123456@localhost/bothub_db')

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/static')


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'bot@amber.sh'
EMAIL_HOST_PASSWORD = '-CS:2;`m8YcAd7Nq'
EMAIL_PORT = 465
EMAIL_USE_SSL = True

MAILER_FROM_EMAIL = 'bot@amber.sh'
MAILER_ADMIN_EMAIL = 'admins@amber.sh'
MAILER_MANAGER_EMAIL = 'managers@amber.sh'


CORS_ORIGIN_WHITELIST = (
    'web-bothub.herokuapp.com',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'lib.framework.rest_api.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=10),
    'JWT_PAYLOAD_HANDLER': 'lib.framework.rest_api.token_management.utils.access_jwt_payload_handler',
}

TOKEN_DEFAULT_SERVICE = 'service'
