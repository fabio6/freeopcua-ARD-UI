# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-30 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcuavars', '0002_auto_20160525_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='init_val',
        ),
        migrations.AddField(
            model_name='variable',
            name='timestamp',
            field=models.DateTimeField(editable=False, null=True, verbose_name='\xdaltima lectura realizada'),
        ),
        migrations.AddField(
            model_name='variable',
            name='value',
            field=models.CharField(default='', editable=False, max_length=31, verbose_name='Ultima lectura realizada'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variable',
            name='method',
            field=models.CharField(max_length=31, verbose_name='Nombre de la variable en la API'),
        ),
    ]
