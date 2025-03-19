import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob
from dotenv import load_dotenv

# Cargar variables de entorno (.env)
load_dotenv()

# 📂 Carpeta donde están los CSVs (corregida)
CARPETA_CSV = r"C:\Users\sergi\Downloads\AvanzadaDatathon\Datos sintéticos reto 2"

def cargar_csvs(carpeta):
    archivos = glob.glob(os.path.join(carpeta, "*.csv"))  # Encuentra todos los CSV
    df_list = [pd.read_csv(archivo) for archivo in archivos]  # Cargar cada CSV
    df_final = pd.concat(df_list, ignore_index=True)  # Unir todos los CSV
    return df_final

# Cargar todos los CSVs
df = cargar_csvs(CARPETA_CSV)

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