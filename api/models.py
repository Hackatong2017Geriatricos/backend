from django.db import models

# Create your models here.

class OrigenDatos(models.Model):
    nombre = models.CharField(max_length=150)
    url = models.URLField()

class LocalOrigenDatos(models.Model):
    id_referencia = models.IntegerField()
    origen = models.ForeignKey(OrigenDatos)

class Local(models.Model):
    origen_referencia = models.ForeignKey(LocalOrigenDatos)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    url = models.URLField()
    titular = models.CharField(max_length=150)
    cuit = models.CharField(max_length=15)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    email = models.EmailField()
    longitud = models.FloatField()
    latitud = models.FloatField()
    fecha_inscripcion = models.DateField()
    estado_habilitacion = models.CharField(max_length=50)
    ente_habilitador = models.CharField(max_length=150)
    plazas_habilitadas = models.IntegerField()
    fecha_actualizacion = models.DateTimeField()
    fecha_creacion = models.DateTimeField()

class Imagen(models.Model):
    url = models.URLField()
    local = models.ForeignKey(Local)
