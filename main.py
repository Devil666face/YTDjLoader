#!./venv/bin/python
import os
from pathlib import Path

# from waitress import serve
# from config.wsgi import application
# from paste.translogger import TransLogger

from dotenv import load_dotenv


BASE_DIR = Path(os.getcwd()).resolve()

load_dotenv(os.path.join(BASE_DIR, ".env"))


import multiprocessing

from gunicorn.app.wsgiapp import WSGIApplication


class StandaloneApplication(WSGIApplication):
    def __init__(self, app_uri, options=None):
        self.options = options or {}
        self.app_uri = app_uri
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = os.getenv("PORT", "8000")
    workers = os.getenv("WORKERS", (multiprocessing.cpu_count() * 2) + 1)
    accesslog = os.getenv("ACCESSLOG", "-")
    errorlog = os.getenv("ERRORLOG", "-")
    keyfile = os.getenv("KEYFILE", False)
    certfile = os.getenv("CERTFILE", False)

    options = {
        "host": host,
        "port": port,
        "workers": workers,
        "accesslog": accesslog,
        "errorlog": errorlog,
    }
    if keyfile:
        options["keyfile"] = keyfile
    if certfile:
        options["certfile"] = certfile
    StandaloneApplication("config.wsgi:application", options).run()

    # serve(TransLogger(application), host=host, port=port)

"""Imports for nuitka"""
import fractions  # noqa
import pytube  # noqa
import django_htmx  # noqa
import django_htmx.middleware  # noqa
