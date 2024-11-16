#Aritmeticos
numero1=2
numero2=4

#BASICOS
print("Operadores Bascios aritmeticos \n")
print(f'Suma  {numero1+numero2}')
print(f'Resta  {numero1-numero2}')
print(f'Multiplicacion   {numero1*numero2}')
print(f'División   {numero2/numero1}')

#Exponent,Modulo y Division entera
print("\nOtros Operadores aritmeticos \n")
print(f'Exponente  {numero1**numero2}')
print(f'Modulo   {numero2%numero1}')
print(f'División Entera  {numero2//numero1}')


#Comparación
print("\nOperadores de Comapración \n")
print(f' 2 Igual que 4 {numero1==numero2}')
print(f' 2 Diferente que 4 {numero1!=numero2}')
print(f' 2 Mayor que 4 {numero1>numero2}')
print(f' 2 Menor que 4 {numero1<numero2}')
print(f' 2 Mayor o igual que 4 {numero1>=numero2}')
print(f' 2 Menor o igual que 4 {numero1<=numero2}')

print("\nOperadores Logicos \n")
print(f' ¿2 es menor que 4 y menor que 7? {numero1<numero2 and numero1<7} ')
print(f' ¿2 es menor que 4 o menor que 1? {numero1<numero2 or numero1<1} ')
print(f' ¿2 no es menor que 4? {not(numero1<numero2)} ')

print("\nOperadores Asinacion \n")
numero3 = 3
numero3 = 5
numero3 +=5
numero3 -=5
print(f'Asignamos 3 luego asignamos 5 sumamos 5 y restamos 5 es igual a: {numero3}')

print("\nOperadores Especiales \n")

print(f'5 es un numero entero: {type(numero3) is int}')
print(f'5 no es un numero entero: {type(numero3) is not int}')
lista=[1,2,3,4,5]
print(f'5 esta en la lista: {5 in lista}')
print(f'5 esta en la lista: {5 not in lista}')
