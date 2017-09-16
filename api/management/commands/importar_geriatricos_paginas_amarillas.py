#!/usr/bin/python
"""
Importar geriatricos desde el API de la Municipalidad de Córdoba
ejecutar como python manage.py importar_geriatricos_paginas_amarillas
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
import os
import sys
import datetime
import requests
import json
from api.models import *

class Command(BaseCommand):
    help = """Comando para Importar Geriátricos scrapeados desde Páginas Amarillas"""

    # solo va a grabar si el proceso se ejecuto completamente sin errores
    @transaction.atomic
    def handle(self, *args, **options):
        file_name = os.path.abspath('./data/paginasamarillas_geriatricos.json')
        with open(file_name) as file:
            data = json.load(file)
            for ficha in data :
                origen = OrigenDatos(
                    id_referencia = ficha['source']['id'],
                    nombre = ficha['source']['type'],
                    url = ficha['source']['url']
                )
                origen.save()

                local = Local(
                    origen_referencia = origen,
                    nombre = ficha['nombre'] or '',
                    descripcion = ficha['descripcion'] or '',
                    url = ficha['url'] or '',
                    telefono = ficha['telefonos']['destacado'] or '',
                    direccion = ficha['direccion']['streetAddress'] + ' ' + ficha['direccion']['addressLocality']  or '',
                    email = ficha['email'] or '',
                    longitud = ficha['direccion']['geo']['longitude'] or 0,
                    latitud = ficha['direccion']['geo']['latitude'] or 0,
                    estado_habilitacion = 'NO_VERIFICADO',
                    titular = '',
                    cuit = '',
                    fecha_inscripcion = timezone.now(),
                    ente_habilitador = 'N/A',
                    plazas_habilitadas = 0,
                    fecha_creacion = timezone.now()
                )
                local.save()

                if ficha['imagen_url'] is not None:
                    imagen = Imagen(
                        url = ficha['imagen_url'],
                        local = local
                    )
                    imagen.save()

                self.stdout.write(self.style.SUCCESS('Local creado con éxito "{}"'.format(local.nombre)))


