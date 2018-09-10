# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-07 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actividades', '0024_merge_20180903_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ofrecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('aceptado', models.PositiveSmallIntegerField(choices=[(-1, 'rechazado'), (0, 'pendiente'), (1, 'aceptado')], default=0)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofrecimientos', to='actividades.Evento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='colaboracion',
            name='vigente',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='participacion',
            name='vigente',
            field=models.NullBooleanField(default=True),
        ),
    ]
