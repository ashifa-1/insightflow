#!/bin/sh

until pg_isready -h postgres -p 5432 -U postgres
do
  echo "Waiting for postgres..."
  sleep 2
done

echo "PostgreSQL started"

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
