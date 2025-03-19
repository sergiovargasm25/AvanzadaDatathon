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

# Crear un contexto basado en los datos combinados
contexto = []
for _, row in datos_combinados.iterrows():
    columnas = ", ".join([f"{key}: {value}" for key, value in row.items()])
    contexto.append(f"Registro - {columnas}")

# Variable de memoria para almacenar las interacciones previas
memoria = []

# Función para responder las consultas
def obtener_respuesta(usuario_input):
    # Agregar la consulta del usuario a la memoria
    memoria.append({"role": "user", "content": usuario_input})
    
    mensajes = [{"role": "system", "content": "Eres un asistente que analiza datos médicos cargados de múltiples CSV. Analiza el contexto de la conversación y sugiere preguntas que puedan guiar la exploración de datos, identificar patrones o refinar la búsqueda de cohortes de pacientes. Asegúrate de que las preguntas propuestas sean relevantes para los datos y útiles para la investigación."}]
    mensajes.append({"role": "user", "content": "\n".join(contexto[:200])})  # Solo los primeros 200 registros para prueba
    
    # Agregar la memoria de interacciones previas
    mensajes.extend(memoria)

    # Obtener la respuesta del modelo
    response = client.chat.completions.create(
        model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
        messages=mensajes
    )

    respuesta = response.choices[0].message.content
    
    # Agregar la respuesta del modelo a la memoria
    memoria.append({"role": "assistant", "content": respuesta})
    
    return respuesta
