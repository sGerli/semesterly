# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-11-26 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0024_auto_20191119_2120"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="pre_health",
            field=models.NullBooleanField(default=False),
        ),
    ]