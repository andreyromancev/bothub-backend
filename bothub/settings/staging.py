from .production import *

IS_PRODUCTION = False
IS_STAGING = True

DEBUG = False
ALLOWED_HOSTS = ['stage-api-bothub.herokuapp.com']
SITE_WEB = 'https://stage-web-bothub.herokuapp.com'

CORS_ORIGIN_WHITELIST = (
    'stage-web-bothub.herokuapp.com',
)
