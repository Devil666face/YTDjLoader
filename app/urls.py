from django.urls import path
from app.views import ModelListView, ModelCreateView

app_name = "app"

urlpatterns = [
    path("", ModelListView.as_view(), name="home"),
    path("create/", ModelCreateView.as_view(), name="create"),
]
