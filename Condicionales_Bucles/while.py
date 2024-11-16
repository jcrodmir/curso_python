print("Uso del While")
x=5
while x > 0:
    x -=1
    print(x)

print("While en una sola linea")    

x = 4

while x > 0: x-=1; print(x)

print("Else tras acabar el while solo si no acaba por break")  
x = 3

while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")