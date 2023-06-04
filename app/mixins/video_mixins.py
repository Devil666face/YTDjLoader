from django.views.generic import (
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


class VideoCreateMixin(VideoMixin, CreateView):
    pass
