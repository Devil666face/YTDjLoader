import os
import re
from pathlib import Path
from dotenv import load_dotenv
from django.template import base

base.tag_re = re.compile(base.tag_re.pattern, re.DOTALL)

BASE_DIR = Path(os.getcwd()).resolve()

load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-*#^gij572j)9sm&b6xnv(7zyy7e*)8m4l)im8l8dd6en^&r71i"
)

DEBUG = False if os.getenv("DEBUG", True) == "False" else True

ALLOWED_HOSTS = ["127.0.0.1", os.getenv("ALLOWED_HOSTS", "*")]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_htmx",
    "app.apps.AppConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

PSQL = True if os.getenv("PSQL", False) == "True" else False

SQLITE_DB = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

POSTGRESQL_DB = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PSQL_NAME", "db"),
        "USER": os.getenv("PSQL_USER", "superuser"),
        "PASSWORD": os.getenv("PSQL_PASSWORD", "Qwerty123"),
        "HOST": os.getenv("PSQL_HOST", "localhost"),
        "PORT": os.getenv("PSQL_PORT", "5432"),
    }
}

DATABASES = POSTGRESQL_DB if PSQL else SQLITE_DB

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache",
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "config/static"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "media/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_COOKIE_DOMAIN = ["127.0.0.1", os.getenv("CSRF_COOKIE_DOMAIN", "*")]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    os.getenv("CSRF_TRUSTED_ORIGINS", "http://*"),
]

CSRF_USE_SESSIONS = True

# SECURE_SSL_REDIRECT = True

# SECURE_SSL_HOST = "https://localhost"
