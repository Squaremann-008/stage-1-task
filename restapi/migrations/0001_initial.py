# Generated by Django 4.1 on 2022-10-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student",
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
                ("slackUsername", models.CharField(max_length=100)),
                ("bio", models.TextField(max_length=100)),
                ("age", models.IntegerField()),
                ("backend", models.BooleanField(default=True)),
            ],
        ),
    ]
