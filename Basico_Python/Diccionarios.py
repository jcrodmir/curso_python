#Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.
#Forma normal de crear

print("DINAMICOS  / INDEXADOS / ANIDADOS")
diccionario={
    "Nombre":"Sara",
    "Edad":34,
    "Casado":False,
}
print(diccionario)

#Otra Forma normal de crear

diccionario2=dict([
    ("Nombre","Carlos"),
    ("Edad",34),
    ("Casado",False),
])
print(diccionario2)

#Otra Forma normal de crear

diccionario3=dict(
    Nombre="Felipe",
    Edad=34,
    Casado=False,
)
print(diccionario3)

print("\nFormas de acceder a diccionarios \n")
print(diccionario["Nombre"])
print(diccionario2.get("Nombre"))
print("\nModificamos diccionario 3")
diccionario3["Nombre"]="Paco"
print(diccionario3["Nombre"])
print("\nAgragamos Key  DNI a diccionario 3")
diccionario3["DNI"]="123456789A"
print(diccionario3)


print("\nIterar diccionarios \n")
print("\nSolo KEYS")
for x in diccionario3:
    print(x)
print("\nSolo VALUES ")
for x in diccionario3:
    print(diccionario3[x])
print("\nAMBOS ")
for x,y in diccionario3.items():
    print(f"Clave es: {x} y  el valor es: {y}")
    

print("\nMetodos diccionarios \n")
print("CLEAR: vacia el diccionario")
print("GET: Devuelve valor con la key")
print(diccionario.get('z', 'No esta dentro diccionario'))
print("ITEMS: Devuelve una lista con keys y values")
print("KEYS: Devuelve todas las claves")
print("VALUES: Devuelve todos los valores")
print("POP: busca y elimina la key que se pasa como parámetro y devuelve su valor asociado")
d = {'a': 1, 'b': 2}
print(d)
d.pop('a')
print(d) #{'b': 2}
print("POPITEM: elimina de manera aleatoria un elemento del diccionario")
print("UPDATE: actualiza con otros valores diccionario")
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}

 
