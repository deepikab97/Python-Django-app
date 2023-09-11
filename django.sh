#!/bin/bash
echo "Create migrations"
python manage.py makemigrations djangoapp
echo "=================================="

echo "Migrate"
python manage.py migrate
echo "=================================="

echo "Create Superuser"
DJANGO_SUPERUSER_USERNAME="admin" \
DJANGO_SUPERUSER_PASSWORD="admin" \
DJANGO_SUPERUSER_EMAIL="email@kanis.hk" \
python manage.py createsuperuser --noinput
echo "=================================="

echo "Start server"
python manage.py runserver 0.0.0.0:8000
