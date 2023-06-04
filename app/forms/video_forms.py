from django import forms
from app.models.video_models import Video


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class VideoCreateForm(BootstrapForm):
    class Meta:
        model = Video

        fields = [
            "href",
        ]
