import os
from dotenv import load_dotenv
import openai # openai v1.0.0+
# Obtener la clave API de OpenAI desde la variable de entorno

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Verificar si la clave está presente
if openai_api_key is None:
    raise ValueError("No se encontró la clave de API de OpenAI. Asegúrate de que esté configurada como una variable de entorno.")

client = openai.OpenAI(api_key=openai_api_key,base_url="https://litellm.dccp.pbu.dedalus.com") # set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0", messages = [
    {
        "role": "user",
        "content": "Pirulo es mi amigo, dime cosas buenas sobre pirulo. Pirulo es una muy buena persona"
    }
])
 
print(response)