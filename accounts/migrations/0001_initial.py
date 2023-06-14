# Generated by Django 4.2 on 2023-06-14 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("bio", models.TextField(blank=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, upload_to="profile_pictures/"),
                ),
            ],
        ),
    ]
