import pandas as pd
import numpy as np

momento=pd.to_datetime("21/10/2024",dayfirst=True)

#Pasamos la fecha a String
print(momento.strftime("%d-%m-%Y"))

#Extraer Mes,año,dia
print(momento.day)
print(momento.month)
print(momento.year)

print(type(momento))
archivo_csv= pd.read_csv("Pandas/consumo_electrico_aleman.csv")
df= pd.DataFrame(archivo_csv)

df.index=df["Date"]
print(df.info())
print(df.head())
print(type(df.index[0]))

df_2014=df.loc["2014":]
df_2014_03=df.loc["2014-03":]
#Loc
df_2014_03_to_2014_04=df.loc["2014-03":"2014-04"]
print(df_2014)
print(df_2014_03_to_2014_04.describe())


#Fechas