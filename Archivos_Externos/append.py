from io import open
#Los archivos se crean en la raiz del proyecto
archivo_externo=open("Archivos_Externos/documentos/PrimerArchivo.txt","a")

archivo_externo.write("\nLinea número 2")

archivo_externo.close()