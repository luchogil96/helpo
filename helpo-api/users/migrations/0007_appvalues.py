# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_merge_20180710_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppValues',
            fields=[
                ('key', models.TextField(primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
        ),
    ]
