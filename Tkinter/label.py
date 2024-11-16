from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=500, bg="red")
miFrame.pack()

# Cargar la imagen con PhotoImage
imagen = PhotoImage(file="./verde.png")

# Diccionario de datos para el texto
datosLabel = {
    "text": "Texto Prueba",
    "fg": "red",
    "bg": "blue",
    "font": ("Courier", 20)
}

# Diccionario de datos para la imagen
datosImagen = {
    "image": imagen
}

# Crear el label para el texto, pack lo reemplaza todo
miLabel=Label(miFrame, **datosLabel).place(x=0,y=0)

# Crear el label para la imagen y posicionarlo
miLabel2=Label(miFrame, **datosImagen).place(x=100, y=100)

root.mainloop()