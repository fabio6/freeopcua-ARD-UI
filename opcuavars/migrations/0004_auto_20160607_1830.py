# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcuavars', '0003_auto_20160530_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='value',
            field=models.CharField(editable=False, max_length=31, verbose_name='Ultimo valor'),
        ),
    ]
