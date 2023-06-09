from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("app.urls.app_urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("app.urls.auth_urls")),
    path("video/", include("app.urls.video_urls")),
    path("playlist/", include("app.urls.playlist_urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
