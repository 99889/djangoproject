web:gunicorn CCMS.wsgi --log-file -
web: python manage.py runserver 0.0.0.0:$PORT --noreload
web: gunicorn hellodjango.wsgi