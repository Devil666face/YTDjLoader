from typing import Any, Dict
from django.views.generic import (
    CreateView,
    ListView,
    View,
)
from django.urls import reverse_lazy
from app.forms.playlist_forms import PlaylistCreateForm
from app.mixins.video_mixins import (
    LoginMixin,
    VideoCreateMixin,
    VideoListViewMixin,
)
from app.models.playlist_models import Playlist
from app.views.video_views import VideoCreateView


class PlaylistMixin(LoginMixin, View):
    model = Playlist
    form_class = PlaylistCreateForm
    template_name = "base.html"


class PlaylistListViewMixin(PlaylistMixin, VideoListViewMixin):
    pass


class PlaylistCreateMixin(PlaylistMixin, VideoCreateView):
    template_name = "app-form.html"
    form_id = "playlistForm"
    button_text = "Create"
