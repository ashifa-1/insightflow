#!/bin/sh
echo "Waiting for PostgreSQL..."
until python manage.py migrate --check >/dev/null 2>&1
do
  sleep 2
done
echo "Database ready"
python manage.py migrate
python manage.py runserver 0.0.0.0:8000