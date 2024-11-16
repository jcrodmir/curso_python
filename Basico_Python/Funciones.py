#Funciones Propias
print("Creamos la Función propia que devuelve un nombre")

def muestraNombre(nombre):
    print(nombre)
    
def resultadoSuma(n1,n2):
    return n1+n2

muestraNombre("Máximo")
print(resultadoSuma(2,2))
print("Uso de funcion no posicional")
print(resultadoSuma(n2=5,n1=2))

print("Uso de Argumentos por defecto")

def suma(a, b, c=0):
    return a+b+c
print(suma(5,5,3)) # 13 ya que a c le pasamos 3
print(suma(5,5)) # 10 ya que al ser por defecto se queda con el 0

print("Uso de * para introducir todos los valores que queramos")
def multiplica(*numeros):
    
    total = 1
    for n in numeros:
        total *= n
    return total
print(multiplica(1, 2, 3, 4)) # 24

print("Uso de ** para introducir todos los valores que queramos en modo diccionario")
def suma2(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma
#letras son keys y numeros values
print(suma2(a=5, b=20, c=23)) # 48
#Si se introduce diccionario se debe meter con **
dic={"a":5,"b":10}
print(suma2(**dic))

#Anotaciones en las funciones que son meramente informativas, se podria introducir otra cosa
def multiplica_por_3(numero: int) -> int:
    return numero*3


print(multiplica_por_3(6))
print(multiplica_por_3("Hola"))
