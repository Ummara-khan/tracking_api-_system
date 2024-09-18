# Generated by Django 5.1.1 on 2024-09-18 06:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TrackingNumber",
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
                ("tracking_number", models.CharField(max_length=16, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("origin_country_id", models.CharField(max_length=2)),
                ("destination_country_id", models.CharField(max_length=2)),
                ("weight", models.DecimalField(decimal_places=3, max_digits=6)),
                ("customer_id", models.UUIDField(default=uuid.uuid4)),
                ("customer_name", models.CharField(max_length=255)),
                ("customer_slug", models.SlugField()),
            ],
        ),
    ]
