import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import json
from .models import Concesion


def obtener_informacion():
    ruta = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta, "datos.json")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximizar la ventana del navegador

    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.concesionesmaritimas.cl/")

    # Cambiar al iframe
    iframe = driver.find_element(By.XPATH, "//frame[@name='centro_sigmar']")
    driver.switch_to.frame(iframe)

    # Aplicar los filtros
    wait = WebDriverWait(driver, 10)  # Aumentar el tiempo de espera si es necesario

    wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='variableRegion']")))
    select_region = Select(driver.find_element(By.XPATH, "//select[@name='variableRegion']"))
    select_region.select_by_value("2")

    wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='variableGobmar']")))
    select_gobernacion = Select(driver.find_element(By.XPATH, "//select[@name='variableGobmar']"))
    select_gobernacion.select_by_visible_text("Antofagasta")

    wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='variableCapuerto']")))
    select_capuerto = Select(driver.find_element(By.XPATH, "//select[@name='variableCapuerto']"))
    select_capuerto.select_by_visible_text("Antofagasta")

    driver.find_element(By.NAME, "verlistado").click()

    # Esperar a que se cargue la tabla (ajusta el tiempo según sea necesario)
    time.sleep(60)

    # Obtener todas las filas de la tabla
    rows = driver.find_elements(By.XPATH, "//table//tr")

    # Crear una lista para almacenar los datos
    data = []

    # Iterar sobre las filas y extraer la información de las celdas
    for row in rows[1:]:
        cells = row.find_elements(By.XPATH, ".//td")
        item = {
            "numero": cells[0].text,
            "enlace": cells[1].find_element(By.TAG_NAME, "a").get_attribute("href"),
            "tipo": cells[2].text,
            "gobernacion_maritima": cells[3].text,
            "lugar": cells[4].text,
            "ds": cells[5].text,
            "tramite": cells[6].text,
            "concesionario": cells[7].text,
            "vigencia": cells[8].text
        }
        data.append(item)

        # Guardar los datos en el modelo Concesion
        concesion = Concesion(
            numero=item["numero"],
            enlace=item["enlace"],
            tipo=item["tipo"],
            gobernacion_maritima=item["gobernacion_maritima"],
            lugar=item["lugar"],
            ds=item["ds"],
            tramite=item["tramite"],
            concesionario=item["concesionario"],
            vigencia=item["vigencia"]
        )
        concesion.save()

    # Cerrar el controlador de Selenium
    driver.quit()

    # Guardar los datos en un archivo JSON
    with open(ruta_json, "w") as file:
        json.dump(data, file)
