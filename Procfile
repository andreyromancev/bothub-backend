release: ./manage.py migrate
web: bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c config/gunicorn.conf --pythonpath bothub bothub.wsgi:application --worker-class gevent
worker: bin/start-pgbouncer-stunnel celery -A bothub worker -l info