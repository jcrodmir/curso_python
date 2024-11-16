print("Range se usa con (inicio,fin,salto)")

print(list(range(0,101,25)))
print(list(range(100,-1,-25)))

print("Distintos tipos de for")

for i in range(0,5):
    print(i)
    
for i in "Python":
    print(i)
    

print("Elementos iterables")

from collections import Iterable
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
cadena = "Python"
numero = 10

print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(tupla, Iterable))
print(isinstance(numero, Iterable)) #False

print("Funcion iter() iteradores")
it=iter(lista)
print(it)
print(type(it))
print("Uso next para iterar")
print(next(it))

print("For anidado")
lista2 = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista2:
    for j in i:
        print(j)





