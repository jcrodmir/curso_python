from io import open
#Los archivos se crean en la raiz del proyecto
archivo_externo=open("Archivos_Externos/documentos/PrimerArchivo.txt","w")

archivo_externo.write("Linea número 1")

archivo_externo.close()