from django import forms
from app.forms.video_forms import (
    BootstrapForm,
    VideoCreateForm,
)
from app.models.playlist_models import Playlist


class PlaylistCreateForm(VideoCreateForm):
    class Meta:
        model = Playlist

        fields = [
            "href",
        ]
