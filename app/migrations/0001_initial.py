# Generated by Django 4.2.1 on 2023-07-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Created"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=255,
                        verbose_name="Playlist title",
                    ),
                ),
                ("href", models.URLField(verbose_name="Url to playlist")),
                (
                    "is_downloaded",
                    models.BooleanField(default=False, verbose_name="Download status"),
                ),
                (
                    "video_count",
                    models.IntegerField(default=0, verbose_name="Count of videos"),
                ),
                (
                    "video_init_count",
                    models.IntegerField(
                        default=0, verbose_name="Count of initial videos"
                    ),
                ),
                (
                    "is_all_video_init",
                    models.BooleanField(
                        default=False, verbose_name="All video initial status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Playlist",
                "verbose_name_plural": "Playlists",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Created"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=255,
                        verbose_name="Video title",
                    ),
                ),
                ("href", models.URLField(verbose_name="Url to video")),
                (
                    "is_downloaded",
                    models.BooleanField(default=False, verbose_name="Download status"),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        upload_to="preview/%Y/%m/%d/",
                        verbose_name="Preview",
                    ),
                ),
                (
                    "download_url",
                    models.URLField(blank=True, verbose_name="Download url"),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        upload_to="videos/%Y/%m/%d/",
                        verbose_name="Video file",
                    ),
                ),
                (
                    "playlist",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="app.playlist",
                        verbose_name="Playlist",
                    ),
                ),
            ],
            options={
                "verbose_name": "Video",
                "verbose_name_plural": "Videos",
                "ordering": ["-created_at"],
            },
        ),
    ]
