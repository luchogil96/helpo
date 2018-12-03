# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-01 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0020_actividadestasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='estado',
            field=models.PositiveSmallIntegerField(choices=[(0, 'other'), (1, 'created'), (2, 'in_progress'), (3, 'finalized')], default=1),
        ),
    ]
