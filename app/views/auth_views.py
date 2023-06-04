from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.urls import reverse_lazy
from app.forms.auth_forms import (
    UserLoginForm,
)


class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("video:video_list")


class UserLogout(LogoutView):
    next_page = reverse_lazy("auth:login")


class PasswordChangeView(PasswordChangeView):
    pass


class PasswordChangeDoneView(PasswordChangeDoneView):
    next_page = "/"
    # template_name = ""
