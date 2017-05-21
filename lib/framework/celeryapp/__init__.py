import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')

app = Celery('app')
app.config_from_object('lib.framework.celeryapp.config')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
