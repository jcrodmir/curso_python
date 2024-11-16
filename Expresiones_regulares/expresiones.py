import re

cadena="Daimiel, porque la vida puede ser maravillosa.La vida es corta"

print("Escribe palabra a buscar")
busqueda=input()
regex=re.search(busqueda,cadena)
todas_regex=re.findall(busqueda,cadena)#Lista con todas las coincidencias
if regex:
    print("La palabra " + busqueda + " esta en el texto")
    print("posicion inicial " + str(regex.start()))
    print("posicion final " + str(regex.end()))
    print("posicion inicial-final " + str(regex.span()))

else:
     print("La palabra " + busqueda + " no se encuentra en el texto")