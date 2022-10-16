# Generated by Django 4.1.2 on 2022-10-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("Product", models.CharField(max_length=100)),
                ("Company", models.CharField(max_length=100)),
                ("positive_review_number", models.IntegerField()),
                ("negative_review_number", models.IntegerField()),
                ("total_review", models.IntegerField()),
                ("total_rating", models.FloatField()),
            ],
        ),
    ]
