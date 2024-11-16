#Los sets en Python son una estructura de datos usada para 
# almacenar elementos de una manera similar a las listas, 
# pero con ciertas diferencias.

print("Propiedades de SET")
print("Elementos unicos")
print("Son desordenados")
print("Deben ser inmutables")

print("Ejemplo Set")
s1=set([5,4,3,2,1,2,2,1])
s2={8,4,7,2,1,2,2,1}
print(s1)
print(s2)

for setIndice in s1:
    print(setIndice)
    
print("1 esta dentro del set",1 in s1)

print("Elementos unio, solo elementos distintos")
print(s1|s2)

print("METODOS ADD/REMOVE(LANZA EXCEPCION SI NO LO ENCUENTRA)/DISCARD/")
print("/DISCARD(NO LANZA EXCEPCION)/POP/CLEAR/ ")