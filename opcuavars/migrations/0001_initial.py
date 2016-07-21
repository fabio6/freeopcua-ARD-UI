# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-25 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='Nombre del rel\xe9')),
                ('pin', models.CharField(choices=[('0', 'Patilla 0'), ('1', 'Patilla 1'), ('2', 'Patilla 2'), ('3', 'Patilla 3'), ('4', 'Patilla 4'), ('5', 'Patilla 5'), ('6', 'Patilla 6'), ('7', 'Patilla 7'), ('8', 'Patilla 8'), ('9', 'Patilla 9'), ('10', 'Patilla 10'), ('11', 'Patilla 11'), ('12', 'Patilla 12'), ('13', 'Patilla 13')], max_length=1)),
                ('state', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Rel\xe9',
                'verbose_name_plural': 'Rel\xe9s',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='Nombre de la variable')),
                ('method', models.CharField(max_length=31, verbose_name='Nombre del m\xe9todo de la API')),
                ('init_val', models.CharField(max_length=31, verbose_name='Valor inicial mientras se obtienen valores reales')),
            ],
            options={
                'verbose_name': 'Variable',
                'verbose_name_plural': 'Variables',
            },
        ),
    ]