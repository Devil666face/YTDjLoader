from typing import (
    Dict,
    List,
    Optional,
)
from pytube import Playlist
from config.settings import MEDIA_ROOT


class PlaylistAPI(Playlist):
    def __init__(self, url: str, proxies: Optional[Dict[str, str]] = None):
        super().__init__(url, proxies)

    @property
    def title(self) -> str:
        return super().title

    @property
    def video_list(self) -> List[str]:
        return [video.watch_url for video in self.videos]
