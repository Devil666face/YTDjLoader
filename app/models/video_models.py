from typing import (
    Any,
    Iterable,
    Optional,
)
from app.models.base_models import BaseModel
from app.utils.video_utils import YouTubeAPI
from app.utils.thread_utils import threadpool
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


class Video(BaseModel):
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        verbose_name="Video title",
    )
    href = models.URLField(
        verbose_name="Url to video",
    )
    is_downloaded = models.BooleanField(
        default=False,
        verbose_name="Download status",
    )
    preview = models.ImageField(
        upload_to="preview/%Y/%m/%d/",
        blank=True,
        verbose_name="Preview",
    )
    download_url = models.URLField(
        blank=True,
        verbose_name="Download url",
    )
    file = models.FileField(
        upload_to="videos/%Y/%m/%d/",
        verbose_name="Video file",
        blank=True,
    )
    playlist = models.ForeignKey(
        "Playlist",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Playlist",
        db_index=True,
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("video:video", kwargs={"pk": self.pk})

    @threadpool
    def api(self):
        if not self.href:
            return
        _ = YouTubeAPI(url=self.href)
        self.title = _.title
        self.preview = _.preview(
            file_path=self.preview.field.generate_filename(self, f"{self.title}.jpg")
        )
        self.download_url = _.download_url
        with transaction.atomic():
            self.save()
        if self.playlist == None:
            return
        self.successful_init_video_for_playlist()

    def successful_init_video_for_playlist(self) -> None:
        from app.models.playlist_models import Playlist

        playlist = Playlist.objects.get(pk=self.playlist.pk)
        playlist.video_init_count += 1
        with transaction.atomic():
            playlist.save()

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ["-created_at"]


@receiver(post_save, sender=Video, dispatch_uid="update_instance_for_api")
def update_instance_for_api(sender, instance, **kwargs):
    if instance.title != "":
        return
    instance.api()
