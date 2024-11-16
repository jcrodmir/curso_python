import pandas as pd
import numpy as np
import json 

archivo_csv= pd.read_csv("Pandas/aguacate.csv")
archivo_excel=pd.read_excel("Pandas/Aguacate producción.xlsx")
df= pd.DataFrame(archivo_csv)

print(df["Year"].mean())
print("-------------------------------------------------------------")
print(df["Year"].std())
print("-------------------------------------------------------------")
print(df["Year"].value_counts())
print("-------------------------------------------------------------")
print(df[" County"].value_counts())
print("-------------------------------------------------------------")
df.rename(columns={" County":"Ciudades"}, inplace=True)
print(df.columns)