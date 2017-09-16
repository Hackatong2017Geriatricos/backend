from django.db import models
import django
# Create your models here.

class OrigenDatos(models.Model):
    id_referencia = models.BigIntegerField()
    nombre = models.CharField(max_length=150)
    url = models.URLField()

class Local(models.Model):
    origen_referencia = models.ForeignKey(OrigenDatos)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    url = models.URLField(blank=True)
    titular = models.CharField(max_length=150)
    cuit = models.CharField(max_length=15)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    longitud = models.FloatField()
    latitud = models.FloatField()
    fecha_inscripcion = models.DateField(blank=True)
    estado_habilitacion = models.CharField(max_length=50)
    ente_habilitador = models.CharField(max_length=150)
    plazas_habilitadas = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(default=django.utils.timezone.now)
    fecha_creacion = models.DateTimeField()

class Imagen(models.Model):
    url = models.URLField()
    local = models.ForeignKey(Local)
