# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 17:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0014_auto_20160622_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishLiked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='posts.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Paper')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dishliked',
            name='like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_by', to='posts.Like'),
        ),
        migrations.AddField(
            model_name='dishliked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_dishes', to=settings.AUTH_USER_MODEL),
        ),
    ]
