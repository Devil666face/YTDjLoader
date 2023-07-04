#!/bin/bash
./venv/bin/python manage.py makemigrations
./venv/bin/python manage.py makemigrations app
./venv/bin/python manage.py collectstatic --no-input
./venv/bin/python manage.py createcachetable
# build project
./venv/bin/python -m nuitka \
--onefile \
--standalone \
--follow-imports \
--include-plugin-directory=./venv/lib/python3.10/site-packages/django \
--include-plugin-directory=./venv/lib/python3.10/site-packages/gunicorn \
--include-plugin-directory=./venv/lib/python3.10/site-packages/whitenoise \
--include-plugin-directory=./config \
--include-plugin-directory=./app \
--include-data-dir=./venv/lib/python3.10/site-packages/django=django main.py
# build manage
./venv/bin/python -m nuitka \
--standalone \
--follow-imports \
--include-plugin-directory=./venv/lib/python3.10/site-packages/django \
--include-plugin-directory=./venv/lib/python3.10/site-packages/whitenoise \
--include-plugin-directory=./config \
--include-plugin-directory=./app \
--include-data-dir=./venv/lib/python3.10/site-packages/django=django manage.py
cp -r ./venv/lib/python3.10/site-packages/django/core manage.dist/django
cp -r ./venv/lib/python3.10/site-packages/django/contrib manage.dist/django
mv manage.dist .manage.dist
ln -s .manage.dist/manage.bin manage.bin
# make release archive
ARCHIVE_NAME="${PWD##*/}.tgz"
cp .dev/install.sh .
cp .dev/ytdjloader.service .
tar -cvzf $ARCHIVE_NAME main.bin manage.bin .manage.dist static/ media/ templates/ install.sh ytdjloader.service
mkdir -p ./dist && mv $ARCHIVE_NAME ./dist
# Use manage.dist/manage.bin migrate for make migrations