from tkinter import *

from tkinter import messagebox as mensaje

root = Tk()

miFrame = Frame(root, width=500, height=500)
miFrame.pack()

miVariable=StringVar()

nombreTexto=Entry(miFrame,textvariable=miVariable)
nombreTexto.grid(row=0,column=1,pady=5,padx=5)
nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0)

passTexto=Entry(miFrame,show="*")
passTexto.grid(row=1,column=1,pady=5,padx=5)
passLabel=Label(miFrame,text="Contraseña: ")
passLabel.grid(row=1,column=0)

emailTexto=Entry(miFrame)
emailTexto.grid(row=2,column=1,pady=5,padx=5)
emailLabel=Label(miFrame,text="Email: ")
emailLabel.grid(row=2,column=0)

direccionTexto=Entry(miFrame)
direccionTexto.grid(row=3,column=1,pady=5,padx=5)
direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=3,column=0)

comentarioLabel=Label(miFrame,text="Comentarios: ")
comentarioLabel.grid(row=4,column=0)
comentarioTexto=Text(miFrame, width=15,height=10)
comentarioTexto.grid(row=4,column=1,pady=5,padx=5)
#Para tener scroll en el texto, donde esta que es el frame comando del texto que queremos con scroll y luego tambien direccion yview vertical
miScroll=Scrollbar(miFrame,command=comentarioTexto.yview)
#Esto hace que ocupe todo el texto con sticky
miScroll.grid(row=4,column=2,sticky="nsew")
#Esto hace esten unidos y el scroll se mueva con el texto
comentarioTexto.config(yscrollcommand=miScroll.set)


def funcionBoton():
    print("Enviado todo")
    #Se hace con messagebox de tkinter que hay que importarlo, primero titulo segundo mensaje
    #mensaje.showinfo("Saludo","Enviado Mensaje")
    nombre=miVariable.get()
    mensaje.showinfo("Saludo",f"Enviado Mensaje \n{nombre}",)
    print(nombre)
    miVariable.set("Juan Carlos")
    comentarioTexto.insert(INSERT,"texto")
    #Imprime desde el inicio hasta el final
    print(comentarioTexto.get(1.0,END))
    
    
#Con command hacemos que el boton haga una accion
boton=Button(miFrame,text="Enviar",command=funcionBoton)
boton.grid(row=5,column=1,pady=5,padx=5)


root.mainloop()