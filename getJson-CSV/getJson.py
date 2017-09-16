import json
import requests

def traer_json_de_url(url):

	respuesta = requests.get(url)
	contenido = respuesta.content.decode("utf8")
	json_desde_url = json.loads(contenido)
	return json_desde_url

def traer_json_junto():

	x = 2

	json_junto = traer_json_de_url("https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/?format=json&tipo_id=1")

	while (True):

		try:

			json_junto["results"] += (traer_json_de_url("https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/?format=json&page={}&tipo_id=1").format(x)["results"])
			
		except Exception as e:

			return json_junto

		x += 1

	return json_junto

def traer_datos_formateados():

	lista_geriatricos = []

	for geriatrico in traer_json_junto()["results"]:

		lista_geriatricos.append([str(geriatrico["nombre"]), str(geriatrico["id"]), str(geriatrico["titular"]), (geriatrico["CUIT"]), str(geriatrico["direccion"]), str(geriatrico["fecha_inscripcion"]), str(geriatrico["estado"]), str(geriatrico["plazas_habilitadas"])])

	return lista_geriatricos	




