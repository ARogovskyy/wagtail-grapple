# Generated by Django 3.1.3 on 2020-12-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0018_add_pagechooserblock")]

    operations = [
        migrations.CreateModel(
            name="SimpleModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        )
    ]
