#!/bin/bash
./venv/bin/python manage.py makemigrations
./venv/bin/python manage.py makemigrations app
./venv/bin/python manage.py collectstatic --no-input
if [ "$SQLITE_BUILD" == "True" ]; then
	./venv/bin/python manage.py migrate
	./venv/bin/python manage.py createcachetable
	export DJANGO_SUPERUSER_PASSWORD=Qwerty123
	./venv/bin/python manage.py createsuperuser --username=superuser --email=artem1999k@gmail.com --no-input
fi
if [ "$SQLITE_BUILD" == "True" ]; then
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
else
	./venv/bin/python -m nuitka \
	--onefile \
	--standalone \
	--follow-imports \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/django \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/gunicorn \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/whitenoise \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/psycopg2 \
	--include-plugin-directory=./config \
	--include-plugin-directory=./app \
	--include-data-dir=./venv/lib/python3.10/site-packages/psycopg2_binary.libs=psycopg2_binary.libs \
	--include-data-dir=./venv/lib/python3.10/site-packages/django=django main.py
	# build manage
	./venv/bin/python -m nuitka \
	--standalone \
	--follow-imports \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/django \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/whitenoise \
	--include-plugin-directory=./venv/lib/python3.10/site-packages/psycopg2 \
	--include-plugin-directory=./config \
	--include-plugin-directory=./app \
	--include-data-dir=./venv/lib/python3.10/site-packages/psycopg2_binary.libs=psycopg2_binary.libs \
	--include-data-dir=./venv/lib/python3.10/site-packages/django=django manage.py
	cp -r ./venv/lib/python3.10/site-packages/django/core manage.dist/django
	cp -r ./venv/lib/python3.10/site-packages/django/contrib manage.dist/django
	mv manage.dist .manage.dist
	ln -s .manage.dist/manage.bin manage.bin
fi
ARCHIVE_NAME="${PWD##*/}.tgz"
ARCHIVE_FILES="main.bin static/ media/ templates/ install.sh ytdjloader.service"
cp .dev/install.sh .
cp .dev/ytdjloader.service .
if [ "$SQLITE_BUILD" == "True" ]; then
	tar -cvzf $ARCHIVE_NAME $ARCHIVE_FILES db.sqlite3
else
	tar -cvzf $ARCHIVE_NAME $ARCHIVE_FILES manage.bin .manage.dist
fi
mkdir -p ./dist && mv $ARCHIVE_NAME ./dist
