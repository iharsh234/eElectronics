# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 20:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0019_paper_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={},
        ),
        migrations.RenameField(
            model_name='like',
            old_name='title',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='date_added',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='likes',
        ),
        migrations.AddField(
            model_name='like',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
