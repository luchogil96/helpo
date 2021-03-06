# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-23 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actividades', '0013_auto_20180719_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('comentario', models.CharField(max_length=140, null=True)),
                ('necesidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colaboraciones', to='actividades.Necesidad')),
                ('voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('comentario', models.CharField(max_length=140, null=True)),
                ('necesidad_voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participaciones', to='actividades.Voluntario')),
                ('voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
