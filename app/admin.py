from typing import Any
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseRedirect
from app.models import (
    Video,
    Playlist,
)
from app.utils.download_utils import Download


class BaseAdminView(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name
            for field in model._meta.fields
            if field.name != "id" and field.name != "title"
        ]
        self.list_display[:0] = ["title"]
        self.list_display_links = ["title", "href"]
        super(BaseAdminView, self).__init__(model, admin_site)


@admin.action(description="Get download script")
def download(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet[Any]
):
    _ = Download(queryset=queryset)
    _.make()
    return HttpResponseRedirect(_.media_url)


class VideoAdminView(BaseAdminView):
    list_filter = ["playlist_id", "is_downloaded"]
    actions = [download]


class PlaylistAdminView(BaseAdminView):
    pass


admin.site.register(Video, VideoAdminView)
admin.site.register(Playlist, PlaylistAdminView)
