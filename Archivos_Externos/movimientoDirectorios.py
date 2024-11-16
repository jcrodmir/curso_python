import os
from io import open
#Creamos directorio
#os.makedirs("Archivos_Externos/Prueba_Directorio_Con_OS")

os.chdir("Archivos_Externos/Prueba_Directorio_Con_OS")
#Directorio actual
print(os.getcwd())

#Archivos en el directorio
print(os.listdir("./"))

#Escribimos archivo
archivo_externo=open("EjemploOS.txt","w")

archivo_externo.write("Hemos creado carpeta y un archivo dentro")

archivo_externo.close()

#Escribimos archivo dos
archivo_externo=open("EjemploOS2.txt","w")

archivo_externo.write("Hemos creado carpeta y un archivo dentro")

archivo_externo.close()

#Renombrar Archivo
os.rename("EjemploOS2.txt","EjemploOSRenombrado.txt")

#Archivos en el directorio
print(os.listdir("./"))

#Borrar Archivo
os.remove("EjemploOSRenombrado.txt")

os.remove("EjemploOS.txt")

os.chdir("../")
#No deja eliminar carpeta con archivos en su interior
os.rmdir("Prueba_Directorio_Con_OS")