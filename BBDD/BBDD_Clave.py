import sqlite3 as sql


miConexion=sql.connect("BBDD/GestionPedidos")

miCursor=miConexion.cursor()
#pRIMARY KEY Y AUTOINCREMENT PARA NO TENER QUE CONTROLAR EL id
'''miCursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")'''
#Para no recrear la tabla varias veces
'''miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")'''

#Insertar un registro
'''miCursor.execute("INSERT INTO PRODUCTOS VALUES('Botella',1,'Bebidas')")'''

#Insertar Varios

ListaProductos=[
    ('Vino',3,'Bebidas'),
    ('Camiseta',12,'Moda'),
    ('Teclado',1,'Informatica')
    
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",ListaProductos)

#Leer Datos
'''miCursor.execute("Select * FROM PRODUCTOS")

listaProductos=miCursor.fetchall()'''

#Borrar datos
'''miCursor.execute("DELETE FROM PRODUCTOS  WHERE ID=3")'''
#Actualizar Datos
'''miCursor.execute("UPDATE PRODUCTOS SET PRECIO=25 WHERE ID=1")'''

##IMPORTANTE CERRAR CURSOR
miCursor.close()

#Solo si se modifica algo
miConexion.commit()

miConexion.close()

#print(listaProductos)