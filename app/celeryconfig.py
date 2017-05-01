import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

if ENVIRONMENT == 'development':
    result_backend = 'cache'
    cache_backend = 'memory'
    broker_url = 'memory://'
    task_always_eager = True
    task_eager_propagates = True
else:
    broker_url = os.environ['REDIS_URL']
    result_backend = os.environ['REDIS_URL']

task_serializer = 'json'
accept_content = ['json']
result_serializer = 'json'

timezone = 'Europe/Moscow'
enable_utc = True
