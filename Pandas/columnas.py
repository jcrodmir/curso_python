import pandas as pd
import numpy as np
import json 

archivo_csv= pd.read_csv("Pandas/aguacate.csv")
archivo_excel=pd.read_excel("Pandas/Aguacate producción.xlsx")
df= pd.DataFrame(archivo_csv)

df.info()
print(df.shape)#420 filas, 11 columnas
print("-------------------------------------------------------------")
print(df.columns)
print("-------------------------------------------------------------")
print(df[" County"])
print("-------------------------------------------------------------")
#Reemplazar columna county pasa a tener datos year
df[" County"]= df["Year"]
print(df)
print("-------------------------------------------------------------")
#Elimanar columna
df.drop([" County"], axis=1, inplace=True)
print(df)
print("-------------------------------------------------------------")
dfFiltrado=list(df.columns)
#Teniendo la lista de columnas removemos la columna y luego aplicamos el filtrado metiendolo como si fuera un indice de la lsita.
#dfFiltrado.remove("Columna")
#df=df[dfFiltrado]



