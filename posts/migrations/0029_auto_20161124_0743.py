# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 02:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_remove_post_read_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='paper',
            name='image',
            field=models.TextField(default='https://eelectronics.herokuapp.com/static/img/product-3.jpg', validators=[django.core.validators.URLValidator()]),
        ),
    ]
