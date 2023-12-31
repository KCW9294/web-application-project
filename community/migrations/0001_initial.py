# Generated by Django 4.2 on 2023-07-02 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rpg", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("file", models.FileField(blank=True, null=True, upload_to="uploads/")),
            ],
        ),
        migrations.CreateModel(
            name="Survey",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField(blank=True, null=True)),
                ("shared", models.BooleanField(default=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        to_field="nickname",
                    ),
                ),
                (
                    "persona_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rpg.persona"
                    ),
                ),
            ],
            options={
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Rating",
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
                ("user_nickname", models.CharField(max_length=100)),
                ("score_1", models.IntegerField()),
                ("score_2", models.IntegerField()),
                ("score_3", models.IntegerField()),
                ("score_4", models.IntegerField()),
                ("score_5", models.IntegerField()),
                ("score_6", models.IntegerField()),
                ("score_7", models.IntegerField()),
                ("score_8", models.IntegerField()),
                ("score_9", models.IntegerField()),
                ("score_10", models.IntegerField()),
                ("score_11", models.IntegerField()),
                ("score_12", models.IntegerField()),
                ("score_13", models.IntegerField()),
                ("score_14", models.IntegerField()),
                ("comment", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="community.survey",
                    ),
                ),
            ],
        ),
    ]
