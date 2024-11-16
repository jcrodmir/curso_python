#Crear lista de python, almacena un conjunto arbitrario de datos. Es equivalente a los Arrays


print("Las listas son: ")
print("Ordenadas")
print("Tipos Arbitrarios")
print("Indexadas[i] ")
print("Anidadas, listas dentro de listas")
print("Mutables, ya que pueden ser modificadas")
print("Dinámicas se pueden añadir y eliminar elementos \n")

#Manera clásica de crear lista
lista = [1,2,3,4]
print(lista)
#Otra manera
lista2= list("1234")
print(lista2)
#Varios valores
lista3=[1,"Hola",True,1.2]
print(lista3)

print("\n Acceso y Modificacion \n")
print(f"Posición 0 lista= {lista[0]}")
lista[0]=2
print(f"Modificamos posicion 0 lista= {lista[0]}")
print(f"Accedemos ultima posicion lista= {lista[-1]}")
del lista[0]
print(f"Eliminamos posicion 0 lista ={lista[0]}")
print(f"Creamos sublista con dos primeras posiciones lista ={lista[0:2]}")
lista[0:2]=[0,0]
print(f"Modificamos sublista con dos primeras posiciones lista ={lista[0:2]}")
lista +=[12,10]
print(f"Agreamos elementos con + a lista ={lista}")
x,y,z=lista[0:3]
print(f"Asignamos 3 primeros elementos con variables de la lista ={x,y,z}")

print("\n Iteración \n")
print("\n Iteración normal ")
for i in lista:
    print(i)

print("\n Iteración normal con indices ")
for index,i in enumerate(lista):
    print(index, i)

print("\n Iteración dos listas a la vez ")
for i,j in enumerate(zip(lista, lista2)):
    print(i,j)

print("\n Iteración Clásica ")
for i in range(0, len(lista)):
    print(lista[i])
    
print("\n Metodos ")
print("\n APPEND \n EXTEND \n INSERT \n REMOVE \n POP \n REVERSE \n SORT \n INDEX")

l = [1, 1, 1, "Hola", 2, 1, 4, 5]
print(l.index("Hola",2)) #5