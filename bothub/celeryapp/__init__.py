import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bothub.settings.development')

app = Celery('app')
app.config_from_object('bothub.celeryapp.config')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
