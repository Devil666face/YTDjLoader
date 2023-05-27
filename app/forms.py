from django import forms
from app.models import Model


class ModelCreateForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = "__all__"
