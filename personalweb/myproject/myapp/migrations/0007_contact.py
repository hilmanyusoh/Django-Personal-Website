# Generated by Django 5.0.2 on 2024-10-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_delete_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("date_sent", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]