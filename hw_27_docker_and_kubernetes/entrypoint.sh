#!/bin/sh

echo "Waiting for PostgreSQL to start..."
while ! nc -z postgres 5432; do
  sleep 1
done

echo "PostgreSQL started, proceeding with Django migrations for PostgreSQL."
# Apply migrations for the default PostgreSQL database
python3 django_docker_project/manage.py migrate --database=default

echo "Waiting for MySQL to start..."
while ! nc -z mysql 3306; do
  sleep 1
done

echo "MySQL started, proceeding with Django migrations for MySQL."
# Apply migrations for the additional MySQL database
python3 django_docker_project/manage.py migrate --database=additional

echo "Starting Django server."
python3 django_docker_project/manage.py runserver 0.0.0.0:8000
