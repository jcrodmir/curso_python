#Generadores devuelven varios valores, no solo uno
#Se almacenan de uno en uno poco a poco
#Desde que entra se queda en stand by
print("GENERADORES")
print("Son más eficientes")
print("Util con listas de valores infinitos")
print("Util generar uno de uno")

#No se necesita limite
def generaNumeroPares():
    num=1
    
    
    while(num>0):
        yield num*2
        num = num + 1 
    
def NumeroPares(limite):
    num=1
    NumeroPares=[]
    while(num<=limite):
        NumeroPares.append(num*2)
        num = num + 1 
        
    return NumeroPares

sucesionPares=generaNumeroPares()
print("Se van dando de uno en uno")
print(next(sucesionPares))
print(next(sucesionPares))
print(NumeroPares(5))

print("Yield from bucle anidado")
def capitalesMundo(*capitales):
    
    for capital in capitales:
        yield capital
        yield from capital
        

capitalesDevueltas=capitalesMundo("Berlin","París","Roma","Madrid","Zagreb")
print("Accedemos a la capital")
print(next(capitalesDevueltas))
print("Accedemos a cada letra de la capital")
print(next(capitalesDevueltas))
print(next(capitalesDevueltas))

print("Forma Alternativa")
lista = [2, 4, 6, 8, 10]
generadorAlCuadrado=(x**2 for x in lista)
print(next(generadorAlCuadrado))
for i in generadorAlCuadrado:
    print(i)

