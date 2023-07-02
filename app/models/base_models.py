from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated",
    )

    class Meta:
        abstract = True
