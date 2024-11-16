import pandas as pd
import numpy as np
import json 

archivo_csv= pd.read_csv("Pandas/aguacate.csv")
archivo_excel=pd.read_excel("Pandas/Aguacate producción.xlsx")
df= pd.DataFrame(archivo_csv)

df.columns = df.columns.str.strip()
print(df.info())
print("-------------------------------------------------------------")
print(df.describe())
print("-------------------------------------------------------------")
print(df.describe(include=[np.number]))
print("-------------------------------------------------------------")
#Cuenta, media, desviacion estanda,minimo,percentiles segun porcentaje analizado, maximo
print(df["County"].describe())
print("-------------------------------------------------------------")
print(df.head())
print("-------------------------------------------------------------")
print(df.tail())
