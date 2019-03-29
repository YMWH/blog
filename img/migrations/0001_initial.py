# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-28 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0003_auto_20190311_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('explain', models.CharField(max_length=200)),
                ('title', models.CharField(default='', max_length=100)),
                ('content', models.CharField(default='', max_length=200)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Course.Course_title')),
            ],
        ),
    ]
