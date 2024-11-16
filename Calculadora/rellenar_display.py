
from tkinter import *

operadores=("+","/","*","-")
operadores_especiales=("+/-","C","CE","M+")
lista=[]
isOperation=False
numero_memoria=0


def dibujar_display(valor,display):
    display.config(state=NORMAL)
    if valor in operadores:
        uso_operadores(display,valor)
    elif valor == "=":
        uso_igual(display)
    elif valor in operadores_especiales:
        uso_operadores_especiales(display,valor)
    else:
        uso_numeros_coma(display,valor)
    display.config(state=DISABLED)

#***********USO NUMEROS Y COMA**************************  
def uso_numeros_coma(display,valor):
    global isOperation
    if display.get()=="0" and valor != "." or(isOperation):
        display.delete(0,END)
        display.insert(0,valor)
        isOperation=False
        
    elif valor != "." or (display.get().find(".")==-1 and valor == "."):
        display.insert(END,valor)
    
    
#***********USO OPERADORES BASICOS**************************     
def uso_operadores(display,valor):
    global isOperation
    isOperation=True
   
    if len(lista)==0:
        lista.append(display.get())
        lista.append(valor)
       
        
    elif len(lista)==2:
        if(lista[1]== valor):
            resultado=calcular(display)
            lista[0]=resultado
           
        else:
            resultado=calcular(display)
            lista[0]=resultado
            lista[1]=valor
    
#***********USO IGUAL**************************      
def uso_igual(display):
    global isOperation
    isOperation=True
    
    if len(lista)==0:
        lista.append(display.get())
        
    elif len(lista)==2:
        calcular(display)
        lista.clear()
        
  
#***********OPERACIONES ESPECIALES**************************      
def uso_operadores_especiales(display,valor):
    global numero_memoria
    if valor == "CE":
       funcion_CE(display)
    elif valor == "C":
        funcion_C(display)
    elif valor == "M+":
        funcion_M(display)    
    elif valor == "+/-":
        funcion_mas_menos(display)

#***********OPERACIONES ESPECIALES FUNCIONES**************************    
def funcion_CE(display):
    lista.clear()  
    numero_memoria == 0
    display.delete(0,END)
    display.insert(0,"0")

def funcion_C(display):
    
    display.delete(0,END)
    display.insert(0,"0")
    
def funcion_M(display):
    
    if numero_memoria == 0 :
        numero_memoria=display.get()
    else:
        display.delete(0,END)
        display.insert(0,numero_memoria)

def funcion_mas_menos(display):
    
    if display.get().find("-")==0:
        display.delete(0,1)
    elif display.get() != "0":
        display.insert(0,"-")


#***********CALCULOS**************************    
def calcular(display):
    
    expresion=f"{lista[0]}{lista[1]}{display.get()}"
    resultado=eval(expresion)
    resultado=comprobar_doble_entero(resultado)
    display.delete(0,END)
    display.insert(0,resultado)
 
    return resultado
              
def comprobar_doble_entero(valor):

    if(valor == int(valor)):
        return int(valor)
    return valor        
       
            
    
        