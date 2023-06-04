from django.contrib import admin
from django.urls import (
    path,
    include,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("app.urls.auth_urls")),
    path("video/", include("app.urls.video_urls")),
]
