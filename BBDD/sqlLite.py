import sqlite3 as sql


miConexion=sql.connect("BBDD/BBDD_Lite")
miCursor=miConexion.cursor()

comprobarTabla= miCursor.execute("SELECT name FROM sqlite_master")

print(comprobarTabla.fetchone())
#Para no recrear la tabla varias veces
'''miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")'''

#Insertar un registro
'''miCursor.execute("INSERT INTO PRODUCTOS VALUES('Botella',1,'Bebidas')")'''

#Insertar Varios
'''
ListaProductos=[
    ('Vino',3,'Bebidas'),
    ('Camiseta',12,'Moda'),
    ('Teclado',1,'Informatica')
    
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",ListaProductos)'''

#Leer Datos
'''miCursor.execute("Select * FROM PRODUCTOS")

listaProductos=miCursor.fetchall()'''


##IMPORTANTE CERRAR CURSOR
miCursor.close()

#Solo si se modifica algo
#miConexion.commit()

miConexion.close()

#print(listaProductos)

