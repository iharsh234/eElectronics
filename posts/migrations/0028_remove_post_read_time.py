# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20161124_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='read_time',
        ),
    ]
