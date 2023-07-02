#!/bin/bash
rm -rf app/migrations/*
rm db.sqlite3
./venv/bin/python manage.py makemigrations app
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createcachetable
export DJANGO_SUPERUSER_PASSWORD=Qwerty123
./venv/bin/python manage.py createsuperuser --username=superuser --email=artem1999k@gmail.com --no-input

