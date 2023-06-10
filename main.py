#!./venv/bin/python
import os
import fractions
from waitress import serve
from config.wsgi import application
from dotenv import load_dotenv
from app.apps import AppConfig

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = os.getenv("PORT", "8080")
    serve(application, host=host, port=port)
