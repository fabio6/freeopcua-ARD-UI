# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcuavars', '0004_auto_20160607_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Nombre')),
                ('dev_type', models.CharField(max_length=1, verbose_name='Tipo')),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
