from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=500)
miFrame.pack()

nombreTexto=Entry(miFrame)
nombreTexto.grid(row=0,column=1)
nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="w")

apellidoTexto=Entry(miFrame)
apellidoTexto.grid(row=1,column=1)
apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1,column=0,sticky="e")

emailTexto=Entry(miFrame)
emailTexto.grid(row=2,column=1)
emailLabel=Label(miFrame,text="Email: ")
emailLabel.grid(row=2,column=0,sticky="n")

direccionTexto=Entry(miFrame)
direccionTexto.grid(row=3,column=1)
direccionLabel=Label(miFrame,text="Dirección mas largo: ")
direccionLabel.grid(row=3,column=0,sticky="s")




root.mainloop()