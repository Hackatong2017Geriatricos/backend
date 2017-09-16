import json
import requests

def traer_json_de_url(url):

	respuesta = requests.get(url)
	contenido = respuesta.content.decode("utf8")
	json_desde_url = json.loads(contenido)
	return json_desde_url

def traer_json_junto():

	proxima_pagina = traer_json_de_url("https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/?format=json&tipo_id=1&page=1")
	print(proxima_pagina["next"])
	json_junto = []

	while (proxima_pagina["next"] != None):

		json_junto += proxima_pagina["results"]

		proxima_pagina = traer_json_de_url(proxima_pagina["next"])

	return json_junto


def traer_datos_formateados():

	lista_geriatricos = []

	lista_geriatricos.append(["nombre", "id", "titular", "cuit", "direccion", "fecha_inscripcion", "estado", "plazas_habilitadas"])
	for geriatrico in traer_json_junto():
		lista_geriatricos.append([str(geriatrico["nombre"].replace(",", " ")), str(geriatrico["id"]), str(geriatrico["titular"].replace(",", " ")), (geriatrico["CUIT"].replace(",", " ")), str(geriatrico["direccion"].replace(",", " ")), str(geriatrico["fecha_inscripcion"].replace(",", " ")), str(geriatrico["estado"].replace(",", " ")), str(geriatrico["plazas_habilitadas"]).replace(",", " ")])
	return lista_geriatricos
