# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-19 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20171119_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='carousel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]
