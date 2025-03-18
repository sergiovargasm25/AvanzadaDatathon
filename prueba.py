import os
from dotenv import load_dotenv
import pandasai as pai

pai.api_key.set("PAI-7b436192-3fdb-411a-9d81-94dd0f12f3fa")
# Load your CSV file
file = pai.read_csv("C:/Users/mipc/Desktop/universidad/2do/2docuatri/hackaton/Datos sintéticos reto 2/cohorte_alegias.csv")

# Save your dataset configuration
df = pai.create(
  path="pai-personal-b3660/dataset-name",
  df=file,
  description="Describe your dataset"
)

# Push your dataset to PandaBI
df.push()