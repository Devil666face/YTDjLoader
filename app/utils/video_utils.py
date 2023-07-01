import os
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
)
from pytube import YouTube
from urllib import request
from config.settings import MEDIA_ROOT

from concurrent.futures import ThreadPoolExecutor
from functools import wraps

_DEFAULT_POOL = ThreadPoolExecutor()


def threadpool(f, executor=None):
    @wraps(f)
    def wrap(*args, **kwargs):
        return (executor or _DEFAULT_POOL).submit(f, *args, **kwargs)

    return wrap


class YouTubeAPI(YouTube):
    def __init__(
        self,
        url: str,
        on_progress_callback: Optional[Callable[[Any, bytes, int], None]] = None,
        on_complete_callback: Optional[Callable[[Any, Optional[str]], None]] = None,
        proxies: Dict[str, str] = None,
        use_oauth: bool = False,
        allow_oauth_cache: bool = True,
    ):
        super().__init__(
            url,
            on_progress_callback,
            on_complete_callback,
            proxies,
            use_oauth,
            allow_oauth_cache,
        )

    @property
    def title(self) -> str:
        return super().title

    def preview(self, file_path: str) -> str:
        full_file_path = Path(MEDIA_ROOT) / file_path
        os.makedirs(full_file_path.parent, exist_ok=True)
        request.urlretrieve(self.thumbnail_url, full_file_path)
        return file_path

    @property
    def download_url(self) -> str:
        url = (
            self.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
            .url
        )
        return url
