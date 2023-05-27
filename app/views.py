from typing import (
    Any,
    Dict,
)
from django import http
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
)
from app.models import Model
from app.forms import ModelCreateForm


class ModelListView(ListView):
    model = Model
    template_name = "home.html"


class ModelCreateView(CreateView):
    model = Model
    form_class = ModelCreateForm
    success_url = reverse_lazy("app:home")
    template_name = "home.html"
