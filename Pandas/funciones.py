import pandas as pd
import numpy as np


def agregar_columna_supervivientes():
    dic={0:"Fallecido", 1:"Superviviente"}
    return dic

def mayus_pasajeros(persona):
    
    return persona.upper()
    
archivo_csv=pd.read_csv("Pandas/titanic.csv")

df= pd.DataFrame(archivo_csv)
#Con map sustituimos cada valor por lo que le digamos survived es 0 y 1
df["supervivientes"]=df["Survived"].map(agregar_columna_supervivientes())
df["mayusculas"]=df["Name"].map(mayus_pasajeros)

#apply_map, es util si queremos transformar todos los valores del dataFrame Sex y Supervivientes en mayusculas

df2=df[["Name","supervivientes"]].applymap(lambda x:x.upper())

#Todo el data frame a mayuscular, siempre que todos sean texto.
df3=df.applymap(lambda x: x.upper() if type(x)==str else x)
print(df.columns)
print(df)

print(df["supervivientes"].value_counts())
print(df2)
print(df3)
