# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-24 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0015_remove_participacion_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaboracion',
            old_name='necesidad',
            new_name='necesidad_material',
        ),
    ]