from django.urls import path
from app.views.playlist_views import (
    PlaylistCreateView,
    PlaylistListView,
)

app_name = "playlist"

urlpatterns = [
    path("<int:playlist_id>/", PlaylistListView.as_view(), name="playlist"),
    path("create/", PlaylistCreateView.as_view(), name="playlist_create"),
]
