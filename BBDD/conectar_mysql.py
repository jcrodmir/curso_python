import mysql.connector as bbdd

miConexion=bbdd.connect(host="localhost",database="delatierra",user="root", password="XDDAW(21)")

miCursor= miConexion.cursor()


miCursor.execute("Select * From producto")

lista= miCursor.fetchall()

miCursor.close()

miConexion.close()

print(lista)