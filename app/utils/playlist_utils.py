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
        self.video_raw_list = self.videos

    @property
    def title(self) -> str:
        return super().title

    @property
    def video_list(self) -> List[str]:
        return [video.watch_url for video in self.video_raw_list]

    @property
    def video_count(self) -> int:
        return len(self.video_raw_list)
