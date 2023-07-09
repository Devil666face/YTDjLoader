import os
from typing import Any, List, Tuple
from django.db.models import QuerySet
from app.models.video_models import Video
from pathlib import Path
from config.settings import MEDIA_ROOT, MEDIA_URL


class Download:
    def __init__(self, queryset: QuerySet[Video]) -> None:
        self.queryset: QuerySet[Video] = queryset

    def make(self):
        self.raw_script = "\n".join(self.get_raw_script_file())
        self.file_path, self.media_path = self.get_file_path(self.file_name)
        self.save_data_in_file(data=self.raw_script, file_path=self.file_path)
        self.set_downloaded_status()

    def set_downloaded_status(self) -> None:
        for video in self.queryset:
            if not video.valid:
                continue
            video.is_downloaded = True
            video.save()

    @property
    def file_name(self) -> str:
        if self.queryset[0].playlist != None:
            return f"{self.queryset[0].playlist_safe}.sh"
        return f"{self.queryset[0].title_safe}.sh"

    @property
    def media_url(self) -> str:
        return "/" + str(self.media_path)

    def get_file_path(
        self, file_name: str, video_empty_obj: Video = Video()
    ) -> Tuple[Path, Path]:
        file_path = video_empty_obj.preview.field.generate_filename(
            video_empty_obj, file_name
        )
        full_file_path = Path(MEDIA_ROOT) / file_path
        os.makedirs(full_file_path.parent, exist_ok=True)
        return full_file_path, MEDIA_URL / Path(file_path)

    def get_raw_script_file(self) -> List[str]:
        bash_sting = ["#!/bin/bash"]
        wget_string = [
            self.get_wget_string(video) for video in self.queryset if video.valid
        ]
        return [*bash_sting, *wget_string]

    def get_wget_string(self, video: Video) -> str:
        return f"wget -O '{video.title_safe}.mp4' '{video.download_url}'"

    def save_data_in_file(self, data: str, file_path: Path) -> None:
        with open(file_path, "w", encoding="UTF-8") as file:
            file.write(data)
