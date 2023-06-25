from typing import (
    Any,
    Callable,
    Dict,
    Optional,
)
from pytube import YouTube


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
