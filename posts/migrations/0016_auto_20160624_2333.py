# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20160624_2315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['-date_added']},
        ),
    ]
