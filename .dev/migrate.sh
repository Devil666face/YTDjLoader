#!/bin/bash
# sudo -u postgres 
PSQL_PREFIX="psql -E -d db -U superuser -h localhost -c"
# rm -rf app/migrations/*
# ./venv/bin/python manage.py makemigrations app
source .env
if [[ "$PSQL" = "True" ]]; then
	$PSQL_PREFIX "DROP SCHEMA public CASCADE;"
	$PSQL_PREFIX "CREATE SCHEMA public;"
	$PSQL_PREFIX "GRANT ALL ON SCHEMA public TO postgres;"
	$PSQL_PREFIX "GRANT ALL ON SCHEMA public TO public;"
else
	rm db.sqlite3
fi
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createcachetable
export DJANGO_SUPERUSER_PASSWORD=Qwerty123
./venv/bin/python manage.py createsuperuser --username=superuser --email=artem1999k@gmail.com --no-input
