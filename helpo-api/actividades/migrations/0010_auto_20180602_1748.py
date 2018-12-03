# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0009_merge_20180529_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacto', to='actividades.Evento'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
