# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-16 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0031_auto_20180914_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='aceptado',
            field=models.SmallIntegerField(choices=[(-1, 'rechazado'), (0, 'pendiente'), (1, 'aceptado')], default=0),
        ),
    ]