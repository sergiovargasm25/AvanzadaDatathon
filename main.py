import os
from dotenv import load_dotenv
import openai

# Cargar variables de entorno
load_dotenv()
Bedrock_api_key = os.getenv("API_KEY")

# Verificar si la clave API está configurada
if Bedrock_api_key is None:
    raise ValueError("No se encontró la clave de API de OpenAI. Asegúrate de que esté configurada como una variable de entorno.")

# Crear cliente de OpenAI con el modelo que sí tienes acceso
client = openai.OpenAI(api_key=Bedrock_api_key, base_url="https://litellm.dccp.pbu.dedalus.com")

print("\n:small_blue_diamond: Escribe tus consultas una por una. Cuando quieras recibir la respuesta, escribe 'responder'.")
print(":small_blue_diamond: Para salir, escribe 'salir'.\n")

mensajes = []

while True:
    prompt = input("> ")

    if prompt.lower() == "salir":
        print(":wave: ¡Hasta luego!")
        break

    if prompt.lower() == "responder":
        print("\n:speech_balloon: Generando respuesta...\n")

        # Enviar mensaje al modelo
        response = client.chat.completions.create(
            model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
            messages=mensajes
        )

        # Mostrar la respuesta del modelo
        print(":robot: Asistente:", response.choices[0].message.content)
        print("\n:small_blue_diamond: Puedes seguir escribiendo más consultas o usar 'responder' otra vez.")
        continue

    # Guardar mensaje del usuario para el contexto
    mensajes.append({"role": "user", "content": prompt})