# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memoryBankApp', '0004_auto_20170309_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listitem',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
