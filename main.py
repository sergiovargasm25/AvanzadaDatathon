import os
import pandas as pd
from dotenv import load_dotenv
import openai

# Cargar variables de entorno
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Verificar si la clave API está configurada
if openai_api_key is None:
    raise ValueError("No se encontró la clave de API de OpenAI. Asegúrate de que esté configurada como una variable de entorno.")

# Crear cliente de OpenAI con el modelo que tengas acceso
client = openai.OpenAI(api_key=openai_api_key, base_url="https://litellm.dccp.pbu.dedalus.com")

# Ruta de la carpeta con los CSV
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

# Cargar datos de todos los archivos en un diccionario
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

# Mostrar información de los datos cargados
print("\nDatos cargados:")
for nombre, df in datos_csv.items():
    print(f"{nombre} - {len(df)} registros")
print("\nTotal de registros combinados:", len(datos_combinados))

# Crear un contexto basado en los datos combinados (ejemplo básico)
contexto = []
for _, row in datos_combinados.iterrows():
    columnas = ", ".join([f"{key}: {value}" for key, value in row.items()])
    contexto.append(f"Registro - {columnas}")

# Simulación de envío de datos al modelo
mensajes = [{"role": "system", "content": "Eres un asistente que analiza datos médicos cargados de múltiples CSV."}]
mensajes.append({"role": "user", "content": "\n".join(contexto[:200])})  # Solo los primeros 200 registros para prueba

# Interfaz con el usuario
print("\n:small_blue_diamond: Datos listos. Escribe tus consultas o usa 'responder' para enviar al modelo. ('salir' para salir)\n")
while True:
    prompt = input("> ")
    if prompt.lower() == "salir":
        print(":wave: ¡Hasta luego!")
        break
    if prompt.lower() == "responder":
        print("\n:speech_balloon: Generando respuesta...\n")
        response = client.chat.completions.create(
            model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
            messages=mensajes
        )
        print(":robot: Asistente:", response.choices[0].message.content)
        continue

    # Añadir la consulta del usuario como mensaje
    mensajes.append({"role": "user", "content": prompt})
