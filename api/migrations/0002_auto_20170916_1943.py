# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha_actualizacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha_inscripcion',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='telefono',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='local',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
