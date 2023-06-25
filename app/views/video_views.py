from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, request, response
from django.urls import reverse_lazy
from django_htmx.http import retarget
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
