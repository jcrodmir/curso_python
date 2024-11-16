from io import open
#Los archivos se crean en la raiz del proyecto salvo que cambiemos direccion
archivo_externo=open("Archivos_Externos/documentos/PrimerArchivo.txt","r")

#Al llegar al 6 termina de leer
#informacionCompleta=archivo_externo.read(6)
informacionCompleta=archivo_externo.read()
#Cursor al principio y se imprimen las dos
archivo_externo.seek(0)
listaConLineas=archivo_externo.readlines()

archivo_externo.close()

print(informacionCompleta)
print(listaConLineas)