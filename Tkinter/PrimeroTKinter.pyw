from tkinter import *

#Creación de ventana
raiz=Tk()
#Moduficaciones
raiz.title("Primera ventana")
#Ni redimensionar ni horizontal ni vertical
raiz.resizable(False,False)
#Icono .ico
raiz.iconbitmap("ico.ico")
#Tamaño que se adapta automaticamente al frame
raiz.geometry("700x400")
#Color Fondo
raiz.config(bg="blue")

#------------------------------------FRAME-------------------------------------------------------------#
miFrame=Frame()
#Side da la posicion ,anchor=cardinal suroeste se, fill rellena horizontal y vertical
miFrame.pack(side=BOTTOM,anchor="se")

miFrame.config(bg="red")

miFrame.config(width="650",height="350")


#bucle infinito para que funciones
raiz.mainloop()

