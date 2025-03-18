import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import LLM  # Importamos la clase base LLM
import os
from dotenv import load_dotenv
import requests  # Para hacer solicitudes HTTP a la API de Bedrock

# Cargar variables de entorno
load_dotenv()
Bedrock_api_key = os.getenv("API_KEY")  # Tu clave de API para Bedrock

# Crear DataFrame de ejemplo
data = {
    "Paciente": ["Juan", "María", "Luis"],
    "Edad": [45, 34, 67],
    "Condición": ["Diabetes", "Hipertensión", "Asma"]
}
df = pd.DataFrame(data)

# Definir una clase personalizada que herede de LLM
class CustomLLM(LLM):
    def __init__(self, api_key, api_base, model):
        super().__init__()
        self.api_key = api_key
        self.api_base = api_base
        self.model = model

    def call(self, prompt):
        # Llamar a la API de Bedrock a través del servicio intermediario
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "model": self.model
        }

        # Hacer la solicitud HTTP
        response = requests.post(
            self.api_base,
            headers=headers,
            json=payload
        )

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Procesar la respuesta de la API
            response_data = response.json()
            # Asegurarse de que la respuesta tenga el formato esperado
            if "response" in response_data:
                return response_data["response"]
            else:
                raise Exception("La respuesta de la API no contiene el campo 'response'")
        else:
            raise Exception(f"Error calling API: {response.status_code}, {response.text}")

    @property
    def _type(self):
        return "custom-llm"

    def chat(self, prompt):
        # Implementar el método chat para cumplir con la interfaz de LLM
        return self.call(prompt)

# Configurar el LLM personalizado
llm = CustomLLM(
    api_key=Bedrock_api_key,  # Tu clave de API
    api_base="https://litellm.dccp.pbu.dedalus.com/v1",  # Tu endpoint
    model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"  # Tu modelo
)

# Crear la instancia de SmartDataframe
smart_df = SmartDataframe(df, config={"llm": llm})

# Hacer una consulta en lenguaje natural
query = "Muestra los pacientes mayores de 40 años."
resultado = smart_df.chat(query)

# Mostrar el resultado
print(resultado)