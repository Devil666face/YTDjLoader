from typing import Any, Iterable, Optional
from uuid import uuid4

from pytube.streams import os
from app.utils.video_utils import YouTubeAPI, threadpool
from django.db import models
from django.urls import reverse
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Video(BaseModel):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Video title",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creatad",
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated",
    )
    href = models.URLField(
        max_length=200,
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

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("video:video", kwargs={"pk": self.pk})

    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Iterable[str]] = ...,
    ) -> None:
        return super().save()

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
        self.save()

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ["-created_at"]


@receiver(post_save, sender=Video, dispatch_uid="update_instance_for_api")
def update_instance_for_api(sender, instance, **kwargs):
    if instance.title:
        return
    instance.api()
