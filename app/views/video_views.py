from django.views.generic import (
    ListView,
    DetailView,
)
from app.mixins.video_mixins import (
    VideoMixin,
    VideoCreateMixin,
)


class VideoListView(VideoMixin, ListView):
    pass


class VideoDetailView(VideoMixin, DetailView):
    pass


class VideoCreateView(VideoCreateMixin):
    pass
