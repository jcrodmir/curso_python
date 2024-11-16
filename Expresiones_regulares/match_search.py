import re


nombre1= "Carlos Rodríguez"
nombre2="Juan Díaz"
nombre3="Sandra Martín"



#match solo lo hace al principio
if re.match(".arlos",nombre1,re.IGNORECASE):
    print("Encontrado")

else:
    print("No he encontrado")
#search lo hace en todo el string

if re.search(".z",nombre1,re.IGNORECASE):
    print("Encontrado")

else:
    print("No he encontrado")