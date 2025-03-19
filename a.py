from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key)

# Cargar un archivo CSV como prueba
df = pd.read_csv("Datos sintéticos reto 2/cohorte_pacientes.csv")

# Convertir el DataFrame a un SmartDataframe
sdf = SmartDataframe(df, config={"llm": llm})

# Hacer una pregunta en lenguaje natural
respuesta = sdf.chat("¿Cuántos pacientes hay en el dataset?")
print(respuesta)