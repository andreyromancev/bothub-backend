import os


redis_url = os.environ.get('REDIS_URL')
if redis_url:
    broker_url = redis_url
    result_backend = redis_url
else:
    result_backend = 'cache'
    cache_backend = 'memory'
    broker_url = 'memory://'
    task_always_eager = True
    task_eager_propagates = True

task_serializer = 'json'
accept_content = ['json']
result_serializer = 'json'

timezone = 'Europe/Moscow'
enable_utc = True
