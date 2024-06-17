# Generated by Django 5.0.4 on 2024-06-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("id_number", models.IntegerField()),
                ("manufacturer", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("year", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("is_sedan", models.BooleanField()),
            ],
        ),
    ]