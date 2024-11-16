#Se crea funcion, con la funcion a añadir como parametro
#Se crea funcion interna con lo que queremos añadir y la funcion que llega por parametro
#Devolvemos la funcion interna y colocamos el decorador en la funcion parametro.
def texto(funcion_parametro):
    
    def funcion_interna(*args,**kwargs):
        print("A continuación realizamos el cálculo")
        
        funcion_parametro(*args,**kwargs)
        
        print("Hemos terminado")
        
    return funcion_interna

#Decorador
@texto
def suma():
    
    print(25+30)
#Decorador con parametros
@texto
def resta(num1,num2):
    
    print(num1-num2)

    
suma()

resta(10,5)