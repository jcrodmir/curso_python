#Tuplas Son inmutables lo que las hace más rápidas que las listas.
#Declaración normal
tupla=(1,2,3,4)
print(tupla)
#Otra forma de declaracion
tupla=4,3,2,1
print(tupla)

#ERROR AL QUERER CAMBIAR VALOR  TypeError: 'tuple' object does not support item assignment  tupla[0]=5

tuplaAnidada=(4,3,(1,2,3),1)
print(tuplaAnidada)

#Es posible convertir lista a tupla y viceversa y asi cambiar datos
tuplaLista=(1,2,3)
print("\n Tupla original")
print(tuplaLista)
listaTupla= list(tuplaLista)
print("Transformacion a  lista")
print(listaTupla)
listaTupla[1]=5
tuplaLista= tuple(listaTupla)
print("Modificamos 2 por 5 y transformamos de nuevo a tupla")
print(tuplaLista)

print("\n Iteración Tupla \n")
for i in tuplaLista:
    print(f"Número {i}")
    
print("\n Variables separadas Tupla \n")
x,y,z=tuplaLista
print(x ,y ,z)


print("\n Métodos Tupla \n")
print("\n Count / Index /  \n")
print("Añadir",tuplaLista.__add__(tupla))
    
    

