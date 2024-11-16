
def funcionExcepcion(name):
    if name in listaPersonas:
        raise ValueError("Error. Este nombre ya se ha introducido")
        
listaPersonas=[]        
contador=0
while contador < 2:	            
    try:
        
        name=str(input("Introduce nombre: "))
        funcionExcepcion(name)
        listaPersonas.append(name)
        contador += 1
        
    except:
        print("Ya has introducido ese nombre")
    
for i in listaPersonas:
    print(i)