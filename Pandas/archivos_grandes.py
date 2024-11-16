import pandas as pd
import numpy as np
import glob 
import re
#Dividir csvs
ruta="Pandas"

archivo_csv= pd.read_csv(ruta + "\\Ventas_online.csv" ,encoding="latin1")


partes_csv= np.array_split(archivo_csv,10)

for indice, df in enumerate(partes_csv):
    df.to_csv(ruta + "\\ventas" + str(indice+1) + ".csv", index=False)

#Unir

ruta_archivos=glob.glob(ruta + "\\*.csv")


archivos_filtrados=[archivo for archivo in ruta_archivos if re.match(r'.*\\ventas\d+\.csv',archivo)]
partes_unir= [pd.read_csv(archivo, encoding="latin1") for archivo in archivos_filtrados]


archivo_final=pd.concat(partes_unir)

archivo_final.to_csv(ruta + "\\ventas_totales.csv", index=False,encoding="latin1")
