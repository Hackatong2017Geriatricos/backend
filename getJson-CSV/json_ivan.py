import csv
from getJson import traer_datos_formateados as traer_datos

def escribir_csv(data, ruta):
    with open(ruta, "w") as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=',')
        for linea in data:
            writer.writerow(linea)

if __name__ == "__main__":
    ruta = "output.csv"
    escribir_csv(traer_datos(), ruta)
