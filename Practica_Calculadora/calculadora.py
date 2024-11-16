from tkinter import * 

def operacion(display,operador):

   if len(lista) == 0 and operador != "=":
       lista.append(display)
       lista.append(operador)
       inicio.set("")
   else:
       lista.append(display)
       expresion=f"{lista[0]}{lista[1]}{lista[2]}"
       resultado=eval(expresion)
       inicio.set(resultado)
       lista.clear()
    
        

def funcionBoton(aux):
    
    operaciones=("+","-","/","*","=")
    
    if aux in operaciones:
        operacion(inicio.get(),aux)
    else:
        if inicio.get()=="0" and aux != ".":
            inicio.set(aux)
        elif inicio.get().find(".")==-1 and aux == ".":
            inicio.set(f"{inicio.get()}{aux}")
        elif aux != ".":
            inicio.set(f"{inicio.get()}{aux}")
    
    

def preparacionCalculadora(botones):
    
    posicionX=1
    posicionY=0
    
    for boton in botones:
        #Funcion lambda cambiar siempre el valor de la variable para que sea por valor y no por referencia
        aux=Button(miFrame,text=boton,command=lambda b=boton: funcionBoton(b),height=2,width=4,background="black",fg="#f0f0f0")
        
        
        if(posicionY%4==0):
            posicionY=0
            posicionX +=1
        aux.grid(row=posicionX,column=posicionY,padx=2,pady=2)
        posicionY +=1
        
        
        
root = Tk()

miFrame = Frame(root, width=400, height=400,background="#555555")
miFrame.pack()
display=Entry(miFrame)
lista=[]
inicio=StringVar()
inicio.set("0")

display.config(background="black",fg="#f0f0f0",justify="right",textvariable=inicio,font=15)
display.grid(row=0,column=0,columnspan=4,pady=10)
botones=("7","8","9","*","4","5","6","+","1","2","3","-",".","0","=","/")
preparacionCalculadora(botones)





root.mainloop()

