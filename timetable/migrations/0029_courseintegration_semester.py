# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-03-31 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0028_course_sub_school"),
    ]

    operations = [
        migrations.AddField(
            model_name="courseintegration",
            name="semester",
            field=models.ManyToManyField(to="timetable.Semester"),
        ),
    ]