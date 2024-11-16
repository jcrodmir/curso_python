import pandas as pd
import numpy as np

#Usamos latin1 para caracteres extraños
archivo_csv= pd.read_csv("Pandas/Ventas_online.csv",encoding="latin1")

df= pd.DataFrame(archivo_csv)

print(df.info())

print(df.isna().sum())

#Muestra de 3000 al azar
datos_ventas=archivo_csv.sample(3000)

print(datos_ventas)
print(df["Pais"].value_counts())

#Agrupar por nombre
print(df.describe())

datos_ventas["FechaCorta"]= pd.to_datetime(datos_ventas["Fecha de factura"])
datos_ventas["FechaCorta"]=datos_ventas["FechaCorta"].apply(lambda x: x.strftime("%Y-%m") if pd.notnull(x) else None )

print(datos_ventas)

#Calculo de total precio

datos_ventas["precio_total"]= datos_ventas["Cantidad"] * datos_ventas["Precio"]

datos_filtrado=datos_ventas[(datos_ventas["precio_total"]>=20) & (datos_ventas["precio_total"]<=30)]
print("---------------------------------------------------------")
print(datos_filtrado)

#Agrupar por mes
datos_filtrado1=datos_filtrado.groupby(["FechaCorta","Pais"], as_index=False).agg({"precio_total":"sum"})

print(datos_filtrado1)

datos_filtrado2=datos_filtrado.groupby(["FechaCorta","Pais"], as_index=False).agg({"N Factura":"count"})

print(datos_filtrado2)

datos_filtrado=datos_filtrado.groupby(["FechaCorta"]).agg({"precio_total":"mean"})

print(datos_filtrado)

datos_filtrado=datos_filtrado.groupby(["FechaCorta"]).agg({"precio_total":"max"})

print(datos_filtrado)

datos_filtrado=datos_filtrado.groupby(["FechaCorta"]).agg({"precio_total":"min"})

print("Minimo",datos_filtrado)

datos_filtrado=datos_ventas.groupby(["FechaCorta"]).agg({"Cantidad":"sum"})

print(datos_filtrado)

datos_filtrado=datos_ventas.groupby(["Pais"]).agg({"Cantidad":"sum"})

import matplotlib.pyplot as plt

datos_filtrado.plot()

plt.show()
