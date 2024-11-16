from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import sqlite3 as sql

window = ThemedTk(theme="arc")


miConexion=sql.connect("Practica_Guiada/BBDD_Lite")
miCursor=miConexion.cursor()

comprobarTabla= miCursor.execute("SELECT name FROM sqlite_master WHERE name='PRODUCTOS'")

print(comprobarTabla.fetchone() )
if comprobarTabla.fetchone is None:
    ttk.Button(window,text="Crear").pack()
    miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
    
else: 
    ttk.Button(window,text="Conectar").pack()
    
miCursor.close()
miConexion.close()
window.mainloop()