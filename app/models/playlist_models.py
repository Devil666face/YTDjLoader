from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models.video_models import (
    BaseModel,
    Video,
    threadpool,
)
from django.db import models
from django.urls import reverse
from app.utils.playlist_utils import PlaylistAPI


class Playlist(BaseModel):
    title = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name="Playlist title",
    )
    href = models.URLField(
        verbose_name="Url to playlist",
    )
    is_downloaded = models.BooleanField(
        default=False,
        verbose_name="Download status",
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("playlist:playlist", kwargs={"pk": self.pk})

    @threadpool
    def api(self):
        if not self.href:
            return
        _ = PlaylistAPI(url=self.href)
        self.title = _.title
        (Video(href=url, playlist=self).save() for url in _.video_list)
        self.save()

    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        ordering = ["-created_at"]


@receiver(post_save, sender=Playlist, dispatch_uid="update_instance_for_api")
def update_instance_for_api(sender, instance, **kwargs):
    if instance.title != "":
        return
    instance.api()
