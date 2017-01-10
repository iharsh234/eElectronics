# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-22 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20160621_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paper',
            options={'ordering': ['-year']},
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='read_time',
            new_name='year',
        ),
        migrations.AddField(
            model_name='paper',
            name='author',
            field=models.TextField(default='harsh'),
        ),
    ]
