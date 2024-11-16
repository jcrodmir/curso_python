from io import open
#Los archivos se crean en la raiz del proyecto salvo que cambiemos direccion
archivo_externo=open("Archivos_Externos/documentos/PrimerArchivo.txt","r")

#Solo se puede usar un read ya que saca la información del archivo externo y no vuelve
#informacionCompleta=archivo_externo.read()
#linea1=archivo_externo.readline()
listaConLineas=archivo_externo.readlines()

archivo_externo.close()

#print(informacionCompleta)
#print(linea1)
print(listaConLineas)