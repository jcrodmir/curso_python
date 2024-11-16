import re

lista_nombres=["Pepe Lopéz","Rodrigo Rodríguez","Ana Millán","Carlos Rodríguez", "Pepe Castro"]
urls=["Pildorainformaticas.es","Pildorainformaticas.com","Pildorainformaticas.net", "informaticas.com"]
lista_terminos=["camión","camion","niños","niñas", "ejemplo"]
lista_acronimos=["MA1","SE1","MA1","MA3", "SE2","MAA","MAB"]

#^ Empieza por lo que sea
#$ finaliza por lo que sea
#[] para buscar más de una opcion
#Rango de letras [letra 1- letra 2]
print("****************[^Inicio - $Final]****************************")       
for nombre in lista_nombres:
    if re.findall("^Pepe",nombre):
        print("Inicio " +nombre)
    
    if re.findall("Rodríguez$",nombre):
        print("Final "  + nombre)
print("****************[Urls]****************************")       
for nombre in urls:
    
    if re.findall(".com$",nombre):
        print(nombre)
print("**************Corchetes[letras concretas]******************************")
for nombre in lista_terminos:
    
    if re.findall("cami[oó]n",nombre):
        print(nombre)
    
    if re.findall("niñ[oa]s",nombre):
        print(nombre)
print("************Rango[l-p]********************************")
for nombre in lista_terminos:
    
    if re.findall("[p-z]",nombre):
        print(nombre)

print("************Rango Inicial^[a-d]********************************")
for nombre in lista_terminos:
    
    if re.findall("^[a-d]",nombre):
        print(nombre)

print("************Rango Inicial^[a-d]********************************")
for nombre in lista_terminos:
    
    if re.findall("[a-o]$",nombre):
        print(nombre)

print("************Rango númerico MA[Rango númerico]********************************")
for nombre in lista_acronimos:
    
    if re.findall("^MA[1-2]$",nombre):
        print(nombre)

print("************Rango númerico negativo MA[^Rango númerico]********************************")
for nombre in lista_acronimos:
    
    if re.findall("^MA[^1-2]$",nombre):
        print(nombre)
        
print("************Rango númerico MA[Rango númerico]********************************")
for nombre in lista_acronimos:
    
    if re.findall("^MA[1-2A-B]",nombre):
        print(nombre)
    
