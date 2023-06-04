from django.urls import path
from app.views.video_views import (
    VideoCreateView,
    VideoDetailView,
    VideoListView,
)

app_name = "video"

urlpatterns = [
    path("<int:pk>/", VideoDetailView.as_view(), name="video"),
    path("list/", VideoListView.as_view(), name="video_list"),
    path("create/", VideoCreateView.as_view(), name="video_create"),
]
