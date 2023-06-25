from typing import Any, Dict
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    View,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from app.forms.video_forms import VideoCreateForm
from app.models.video_models import Video


class LoginMixin(LoginRequiredMixin):
    login_url = reverse_lazy("auth:login")


class VideoMixin(LoginMixin, View):
    model = Video
    form_class = VideoCreateForm
    template_name = "base.html"


class VideoListViewMixin(VideoMixin, ListView):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        extra_context = {
            "video_create_form": VideoCreateForm(),
        }
        return {**super().get_context_data(**kwargs), **extra_context}


class VideoCreateMixin(VideoMixin, CreateView):
    template_name = "form-video.html"
    success_url = reverse_lazy("video:video_list")