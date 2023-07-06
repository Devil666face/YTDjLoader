from django.views.generic import (
    View,
)
from app.forms.playlist_forms import PlaylistCreateForm
from app.mixins.video_mixins import (
    LoginMixin,
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
