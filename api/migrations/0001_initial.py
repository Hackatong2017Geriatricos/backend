# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('titular', models.CharField(max_length=150)),
                ('cuit', models.CharField(max_length=15)),
                ('telefono', models.CharField(blank=True, max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('longitud', models.FloatField()),
                ('latitud', models.FloatField()),
                ('fecha_inscripcion', models.DateField(blank=True)),
                ('estado_habilitacion', models.CharField(max_length=50)),
                ('ente_habilitador', models.CharField(max_length=150)),
                ('plazas_habilitadas', models.IntegerField()),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_creacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OrigenDatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_referencia', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='local',
            name='origen_referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.OrigenDatos'),
        ),
        migrations.AddField(
            model_name='imagen',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Local'),
        ),
    ]
