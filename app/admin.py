from django.contrib import admin
from app.models.video_models import (
    Video,
)


class BaseAdminView(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"
        ]
        super(BaseAdminView, self).__init__(model, admin_site)


class VideoAdminView(BaseAdminView):
    pass


admin.site.register(Video, VideoAdminView)
