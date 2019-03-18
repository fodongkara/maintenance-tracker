release: python manage.py makemigrations && python manage.py migrate
web: gunicorn maintenance_tracker.wsgi --log-file -
