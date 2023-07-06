from typing import Any, Dict
from django.db.models import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django_htmx.http import HttpResponseClientRedirect
from app.models.playlist_models import Playlist
from app.mixins.playlist_mixins import (
    PlaylistListViewMixin,
    PlaylistCreateMixin,
)
from app.views.video_views import VideoCreateView, VideoListView
from app.models.video_models import Video


class PlaylistListView(PlaylistListViewMixin, VideoListView):
    model = Video
    template_name = "base-playlist.html"

    def get_queryset(self) -> QuerySet[Any]:
        self.playlist_id = self.kwargs.get("playlist_id", 0)
        return self.model.objects.filter(playlist_id=self.playlist_id).select_related(
            "playlist"
        )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        extra_context = {"playlist_id": self.playlist_id}
        return {**super().get_context_data(**kwargs), **extra_context}


class PlaylistCreateView(PlaylistCreateMixin):
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        valid = super().form_valid(form)
        return HttpResponseClientRedirect(
            reverse_lazy("playlist:playlist", kwargs={"playlist_id": self.object.pk})
        )
