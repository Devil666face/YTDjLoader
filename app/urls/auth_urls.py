from django.urls import path
from app.views.auth_views import (
    UserLogin,
    UserLogout,
    PasswordChangeView,
    PasswordChangeDoneView,
)

app_name = "auth"

urlpatterns = [
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
