import psycopg2 as bbdd

miConexion=bbdd.connect(host="localhost",database="Euro2024",user="postgres", password="XDDAW(21)")

miCursor= miConexion.cursor()


miCursor.execute("Select * From player_entity")

lista= miCursor.fetchall()

miCursor.close()

miConexion.close()

print(lista)
