from typing import Any, Optional
from django.urls import reverse_lazy
from django.views.generic import RedirectView


class AppRedirectView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> Optional[str]:
        redirect_url = super().get_redirect_url(*args, **kwargs)
        return reverse_lazy("video:video_list")
