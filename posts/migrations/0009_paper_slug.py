# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_paper_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='slug',
            field=models.TextField(default='abcd'),
        ),
    ]
