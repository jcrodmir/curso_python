#Se usa para funciones sencillas y que se usan de manera repetitiva.
'''def calcular_area_triangulo(base,altura):
    
    return (base*altura)/2

triangulo1=calcular_area_triangulo(10,5)
triangulo2=calcular_area_triangulo(3,6)'''

area_triangulo= lambda base,altura: (base*altura)/2
print(area_triangulo(10,5))
print(area_triangulo(8,10))

potencia_numero= lambda numero,elevado: numero**elevado
print(potencia_numero(2,3))

comision_formato= lambda comision: (f"¡{comision}!€")
print(comision_formato(5000))

#Ordenar lista
lista=[5,9,2,3,14,26]

ordenar_lista= lambda mi_lista:  mi_lista.sort()#Modifica lista antigua sorted(mi_lista) crea una nueva
ordenar_lista(lista)
print(lista)

