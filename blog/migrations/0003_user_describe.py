# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160831_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='describe',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='自我简介'),
        ),
    ]
