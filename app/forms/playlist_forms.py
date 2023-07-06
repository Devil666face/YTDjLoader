from app.forms.video_forms import (
    VideoCreateForm,
)
from app.models.playlist_models import Playlist


class PlaylistCreateForm(VideoCreateForm):
    class Meta:
        model = Playlist

        fields = [
            "href",
        ]
