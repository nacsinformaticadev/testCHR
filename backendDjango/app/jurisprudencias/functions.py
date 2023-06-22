import requests
from datetime import datetime
from .models import Jurisprudencia

def obtener_jurisprudencia():
    #lamentablemente la url proporsionada es una web en javascript y no un url de peticion API para poder generar el post
    #de todas formas dejo una funcion de ocmo podria extraer la data de fuera correcta la URL
    url = "https://www.buscadorambiental.cl/buscador/jurisprudencia/list"

    # Realizar la petición POST
    response = requests.post(url)

    if response.status_code == 200:
        data = response.json()

        # Obtener la información de la respuesta
        results = data.get("results", [])

        # Recorrer los resultados y guardar en el modelo
        for result in results:
            titulo = result.get("titulo")
            fecha_str = result.get("fecha")

            # Convertir la fecha de texto a objeto de fecha
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

            fuente = result.get("fuente")
            contenido = result.get("contenido")

            # Crear un objeto Jurisprudencia y guardarlo en la base de datos
            jurisprudencia = Jurisprudencia(titulo=titulo, fecha=fecha, fuente=fuente, contenido=contenido)
            jurisprudencia.save()