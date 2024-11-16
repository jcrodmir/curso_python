#Metodos UPPER,LOWER,CAPITALIZE,COUNT,FIND,ISDIGIT ISALNUM, ISALPHA, SPLIT,STRIP,REPLACE, rFIND

cadena= " minuscula a mayuscula "
print(cadena.replace(" ",""))
print(cadena.upper() + " " + cadena.capitalize() )
print(cadena.isdigit() ,  cadena.isalpha()  ,cadena.isalnum())#Da false por los espacios
print(cadena.find("c"))# da Index si lo encuentra
print(cadena.rfind("c"))# da Index si lo encuentra
print(cadena.split(" "))
print(cadena.strip())#Solo si hay espacios al principio o al final