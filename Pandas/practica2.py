import pandas as pd
import json 

archivo_csv= pd.read_csv("Pandas/aguacate.csv")
archivo_excel=pd.read_excel("Pandas/Aguacate producción.xlsx")
df= pd.DataFrame(archivo_csv)

print(df)

#Cargar json

# Abrir el archivo JSON manualmente
with open("Pandas/fichero_covid.json", "r") as file:
    data = json.load(file)

# Verifica que la clave "Countries" exista en el archivo JSON
if "Countries" in data:
    # Convertir la lista de diccionarios en un DataFrame
    df = pd.DataFrame(data["Countries"])
    
    # Mostrar el DataFrame
    print(df)
else:
    print("La clave 'Countries' no se encontró en el archivo JSON")