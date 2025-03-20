import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv

# Cargar variables de entorno (.env)
load_dotenv()

def cargar_csvs():
    # Cargar datos de todos los archivos en un diccionario
    carpeta_csv = "Datos sintéticos reto 2"

    # Lista de archivos CSV a cargar
    archivos_csv = [
        "cohorte_alegias.csv",
        "cohorte_condiciones.csv",
        "cohorte_encuentros.csv",
        "cohorte_medicationes.csv",
        "cohorte_pacientes.csv",
        "cohorte_procedimientos.csv",
        "datos_sinteticos.csv"
    ]

    datos_csv = {}
    for archivo in archivos_csv:
        ruta_archivo = os.path.join(carpeta_csv, archivo)
        if os.path.exists(ruta_archivo):
            print(f"Cargando datos desde: {ruta_archivo}")
            datos_csv[archivo] = pd.read_csv(ruta_archivo)
        else:
            print(f"Archivo no encontrado: {ruta_archivo}")

    # Fusionar los datos en un único DataFrame (opcional, si son combinables)
    datos_combinados = pd.concat(datos_csv.values(), axis=0, ignore_index=True)
    return datos_combinados

# Cargar los datos al inicio
df = cargar_csvs()

def generar_grafico(consulta):
    # Generar histograma
    if "histograma" in consulta.lower():
        columna = consulta.split("de")[-1].strip()
        if columna in df.columns:
            plt.figure(figsize=(8, 5))
            sns.histplot(df[columna], kde=True, bins=30)
            plt.title(f"Histograma de {columna}")
            plt.savefig("grafico.png")
            plt.close()  # Cerrar la figura para liberar memoria
            return "Se ha generado un histograma. Revisa 'grafico.png'."
        else:
            return f"La columna '{columna}' no existe."

    # Generar gráfico de barras
    elif "gráfico de barras" in consulta.lower() or "grafico de barras" in consulta.lower():
        columna = consulta.split("de")[-1].strip()
        if columna in df.columns:
            plt.figure(figsize=(8, 5))
            df[columna].value_counts().plot(kind="bar", color="skyblue")
            plt.title(f"Gráfico de barras de {columna}")
            plt.savefig("grafico.png")
            plt.close()  # Cerrar la figura para liberar memoria
            return "Se ha generado un gráfico de barras. Revisa 'grafico.png'."
        else:
            return f"La columna '{columna}' no existe."

    # Si no se entiende la consulta
    else:
        return None  # Devolver None si no es una consulta de gráfico