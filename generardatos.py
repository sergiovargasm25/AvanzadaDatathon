import os
from faker import Faker
import random
import csv

fake = Faker('es_ES')  # Generar datos en español

# Lista de códigos y descripciones SNOMED
snomed_codes = [
    (91936005, "Alergia al polen"),
    (91933007, "Alergia a los frutos secos"),
    (300913006, "Alergia a la penicilina"),
    (91931005, "Alergia a la leche"),
    (91930004, "Alergia a los ácaros del polvo"),
    (414285001, "Alergia al látex"),
    (91935009, "Alergia al pelo de gato"),
    (91934008, "Alergia a la picadura de abeja"),
    (300914000, "Alergia a la aspirina"),
    (91932006, "Alergia a los mariscos")
]

# Generar datos sintéticos
def generar_datos_sinteticos(numero_de_registros):
    datos = []
    for _ in range(numero_de_registros):
        paciente_id = random.randint(1, 30)  # Generar un ID aleatorio
        fecha_diagnostico = fake.date_between(start_date='-10y', end_date='today')  # Fecha en los últimos 10 años
        codigo_snomed, descripcion = random.choice(snomed_codes)  # Elegir un SNOMED al azar
        datos.append([paciente_id, fecha_diagnostico, codigo_snomed, descripcion])
    return datos

# Guardar los datos en un archivo CSV en una carpeta específica
def guardar_en_csv(datos, nombre_carpeta, nombre_archivo):
    # Crear la carpeta si no existe
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    # Ruta completa del archivo
    ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)
    # Guardar los datos en el archivo
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["PacienteID", "Fecha_diagnostico", "Codigo_SNOMED", "Descripcion"])
        escritor.writerows(datos)
    print(f"Archivo guardado en: {ruta_archivo}")

# Generar y guardar los datos
numero_de_registros = 100  # Ajusta el número de registros que desees generar
datos_sinteticos = generar_datos_sinteticos(numero_de_registros)
guardar_en_csv(datos_sinteticos, "Datos sintéticos reto 2", "datos_sinteticos.csv")

print(f"Se han generado {numero_de_registros} registros sintéticos y guardado en la carpeta 'Datos sintéticos reto 2'.")
