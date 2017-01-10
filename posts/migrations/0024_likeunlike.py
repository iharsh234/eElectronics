# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-30 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0023_auto_20160627_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeUnlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Paper')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
