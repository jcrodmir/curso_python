from io import open
#Los archivos se crean en la raiz del proyecto salvo que cambiemos direccion
archivo_externo_modificar=open("Archivos_Externos/documentos/PrimerArchivo.txt","r")


numeroLineas=archivo_externo_modificar.readlines()
numeroLineas[1]="Linea numero\n"

archivo_externo_modificar.close()

#Los archivos se crean en la raiz del proyecto salvo que cambiemos direccion
archivo_externo_reescribir=open("Archivos_Externos/documentos/PrimerArchivo.txt","w")

archivo_externo_reescribir.writelines(numeroLineas)
archivo_externo_reescribir.close()
#print(informacionCompleta)
#print(linea1)