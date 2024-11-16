from tkinter import *
import rellenar_display as rellenar

class interfaz_calculadora:
    BOTONES=("+/-","C","CE","M+","7","8","9","*","4","5","6","+","1","2","3","-",".","0","=","/")
    
    def __init__(self, root) -> None:
        # Crear el frame principal
        self.miFrame= Frame(root, width=400, height=400,background="#555555")
        self.miFrame.pack()
        
        # Crear el display de entrada
        self.display = Entry(self.miFrame,state=DISABLED)
        self.display.config(disabledbackground="black",disabledforeground="white",justify="right",font=15 )
        self.display.config(state=NORMAL)
        self.display.insert(0,"0")
        self.display.config(state=DISABLED)
        self.display.grid(row=0,column=0,columnspan=4,pady=10)
        
        self.rellenarNumeros()
    

    def valorActual(self,valor):
        
        rellenar.dibujar_display(valor,self.display)
        
    def rellenarNumeros(self):
        
        posicionX=1
        posicionY=0
        
        for boton in self.BOTONES:
            #Funcion lambda cambiar siempre el valor de la variable para que sea por valor y no por referencia
            aux=Button(self.miFrame,text=boton,command= lambda b=boton: self.valorActual(b),height=2,width=4,background="black",fg="#f0f0f0",font=15)
            
            
            if(posicionY%4==0):
                posicionY=0
                posicionX +=1
            aux.grid(row=posicionX,column=posicionY,padx=2,pady=2)
            posicionY +=1
    
    
