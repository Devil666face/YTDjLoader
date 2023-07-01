from typing import Any
from django.db.models import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.urls import reverse_lazy
from django_htmx.http import (
    retarget,
    HttpResponseClientRefresh,
)
from django.views.generic import (
    ListView,
    DetailView,
)
from app.mixins.video_mixins import (
    VideoMixin,
    VideoListViewMixin,
    VideoCreateMixin,
)


class VideoListView(VideoListViewMixin):
    template_name = "base-video.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.htmx and self.request.headers.get("HX-Target", False):
            """If htmx and auto-reload request"""
            self.template_name = "components/video-list.html"
            self.response = super().get(request, *args, **kwargs)
            if all(object.title != "" for object in self.get_queryset()):
                """If all obj after api init -> stop polling"""
                self.response.status_code = 286
                return self.response
        return super().get(request, *args, **kwargs)


class VideoDetailView(VideoMixin, DetailView):
    template_name = "detail-video.html"


class VideoCreateView(VideoCreateMixin):
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        if self.request.htmx:
            extra_context = {
                "action": self.request.path,
                "id": "downloadForm",
                "btn": "Download",
            }
            response = render(
                self.request,
                self.template_name,
                context={**self.get_context_data(), **extra_context},
            )
            return retarget(response, "#downloadForm")
        return super().form_invalid(form)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        valid = super().form_valid(form)
        return HttpResponseClientRefresh()
