import pandas as pd

#Cargar datos diferentes origenes de datos
#trabajar similar tabla dinamica
#transformacion daatos
#calculos por filas
#numpy para analisis de datos visuales
#Exportaciones de datos a difrentes archivos

df= pd.DataFrame({"num_legs":[2,4,4], "num_wings":[2,0,0]}, index=["falcon","dog","cat"])

print(df)