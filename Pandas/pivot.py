import pandas as pd


#Usamos latin1 para caracteres extraños
archivo_csv= pd.read_csv("Pandas/Ventas_online.csv",encoding="latin1")

df= pd.DataFrame(archivo_csv)

print(df.info())

print(df.isna().sum())

#Muestra de 3000 al azar
datos_ventas=archivo_csv.sample(3000)
datos_ventas["Fecha de factura"] = pd.to_datetime(datos_ventas["Fecha de factura"], errors='coerce')
datos_ventas = datos_ventas.dropna(subset=["N Factura", "Fecha de factura", "Precio"])

tabla_pivot=pd.pivot_table(datos_ventas,index="N Factura",columns="Fecha de factura",values="Precio",aggfunc="mean")

print(tabla_pivot)