# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_auto_20171129_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]