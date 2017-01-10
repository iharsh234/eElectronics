# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 08:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0021_auto_20160627_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
