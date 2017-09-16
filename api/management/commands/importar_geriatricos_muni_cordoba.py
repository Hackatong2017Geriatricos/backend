#!/usr/bin/python
"""
Importar geriatricos desde el API de la Municipalidad de Córdoba
ejecutar como python manage.py importar_geriatricos_muni_cordoba
"""
from django.core.management.base import BaseCommand
from django.db import transaction
import sys
import datetime
import requests
import json
from api.models import *


class Command(BaseCommand):
    help = """Comando para Importar geriátricos de la muni """

    '''
    def add_arguments(self, parser):
        parser.add_argument('--ppp', nargs='?', type=str, help='ayuda param')
    '''

    # solo va a grabar si el proceso se ejecuto completamente sin errores
    @transaction.atomic
    def handle(self, *args, **options):
        url = "https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/"
        self.stdout.write(self.style.SUCCESS('Buscando datos desde {}'.format(url)))

        res = []  # resultados a devolver
        while url:
            r = requests.get(url=url)
            self.stdout.write(self.style.SUCCESS('Datos obtenidos desde {}'.format(url)))
            respuesta = r.json()
            resultados = respuesta["results"]
            for resultado in resultados:
                '''
                tomar este geríatrico y grabarlo en la base validando si el ID único en la muni
                no existe
                Registrar cambios en los datos
                '''
                pass

            # en la última página viene vacío
            url = respuesta["next"]

        return res

        # orama, created = RamaActividad.objects.get_or_create(nombre=rama_actividad)
        # ocategoria, created = CategoriaActividad.objects.get_or_create(rama=orama, nombre=categoria)
        # oactividad = ActividadOTA.objects.create(categoria=ocategoria, codigo=codigo, nombre=descripcion, alicuota=alicuota, minimo=minimo)


        self.stdout.write(self.style.SUCCESS('Archivo cargado con éxito, se cargaron {} registros nuevos ({} repetidos)'.format(nuevos, repetidos)))
