#!/bin/bash

# TODO: Remove migrate from here
# Apply database migrations
python manage.py migrate --noinput

# clearstatic files
python manage.py collectstatic --clear --noinput

# collect static files
python manage.py collectstatic --noinput

# Prepare log files and start outputting logs to stdout
tail -n 0 -f /logs/*.log &

# Set up nginx configuration
echo Configuring nginx
# envsubst < /etc/nginx/sites-available/django_nginx.conf > /etc/nginx/sites-enabled/default
# echo "daemon off;" >> /etc/nginx/nginx.conf

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn -w 4 --timeout 60 --max-requests 1000 --chdir /code/app --log-file=/logs/gunicorn.log \
    --access-logfile=/logs/access.log --pythonpath /code wsgi:application -b 0.0.0.0:8000 &

# Start nginx
echo Starting nginx
exec service nginx start

echo Task finished