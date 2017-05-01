release: ./manage.py migrate
web: bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c config/gunicorn.conf --pythonpath app app.wsgi:application
worker: bin/start-pgbouncer-stunnel celery -A app worker -l info