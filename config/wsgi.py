import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
application = WhiteNoise(
    application, root=settings.STATIC_ROOT, prefix="/static/", autorefresh=True
)
application.add_files(root=settings.MEDIA_ROOT, prefix="/media/")
