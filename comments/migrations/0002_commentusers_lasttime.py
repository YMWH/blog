# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-12 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentusers',
            name='lastTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
