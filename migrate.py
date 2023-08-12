#!./venv/bin/python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import argparse
import django

from django.core.management import execute_from_command_line
from django.core.management.commands import migrate
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import call_command

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--migrate", help="migrate database", action="store_true")
parser.add_argument("-s", "--superuser", help="create superuser", action="store_true")

args = parser.parse_args()


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # execute_from_command_line()
    django.setup()
    if args.migrate:
        call_command(migrate.Command())
    elif args.superuser:
        call_command(createsuperuser.Command())
    else:
        print("You dont add options use -h/--help for have info")


if __name__ == "__main__":
    main()
