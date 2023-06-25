import re
from django import forms
from app.models.video_models import Video


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class VideoCreateForm(BootstrapForm):
    start_with_list = (r"https://www.youtube.com/", r"https://www.youtu.be")

    class Meta:
        model = Video

        fields = [
            "href",
        ]

    def clean_href(self):
        href: str = self.cleaned_data["href"]
        for start_pattern in self.start_with_list:
            if re.match(start_pattern, href):
                return href
        raise forms.ValidationError("Url must start with youtube.com or youtu.be")
