# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-22 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20160622_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='author',
            field=models.TextField(default='harsh'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='content',
            field=models.TextField(),
        ),
    ]
