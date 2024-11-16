#

import math

def calculaRaiz(numero):
    
    if(numero < 0):
        raise ValueError("No puede ser negativo")
    else:
        return math.sqrt(numero)

try:
    numeroUsuario=(int(input("Introduce un numero")))
    print(calculaRaiz(numeroUsuario))
except ValueError:
    print("Error por numero negativo")
    

