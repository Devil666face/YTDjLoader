from django.urls import path
from app.views.app_views import AppRedirectView

app_name = "app"

urlpatterns = [
    path("", AppRedirectView.as_view(), name="app"),
]
