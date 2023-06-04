#!/bin/bash
./venv/bin/python manage.py makemigrations
./venv/bin/python manage.py makemigrations app
./venv/bin/python manage.py collectstatic --no-input
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createcachetable
export DJANGO_SUPERUSER_PASSWORD=Qwerty123
./venv/bin/python manage.py createsuperuser --username=superuser --email=artem1999k@gmail.com --no-input
# build project
./venv/bin/python -m nuitka \
--onefile \
--standalone \
--follow-imports \
--include-plugin-directory=./venv/lib/python3.10/site-packages/django \
--include-plugin-directory=./venv/lib/python3.10/site-packages/waitress \
--include-plugin-directory=./venv/lib/python3.10/site-packages/whitenoise \
--include-plugin-directory=./config \
--include-plugin-directory=./app \
--include-data-dir=./venv/lib/python3.10/site-packages/django=django main.py
# make release archive
ARCHIVE_NAME="${PWD##*/}.tgz"
tar -cvzf $ARCHIVE_NAME main.bin static/ media/ templates/ db.sqlite3
mkdir -p ./dist && mv $ARCHIVE_NAME ./dist