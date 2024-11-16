#Son rastreadores de las estructuras basicas.
#Crear una BBDD con la información extraida de las paginas web.
#Examina los enlaces recibidos y externos
from bs4 import BeautifulSoup
import requests

miReq=requests.get("http://www.as.com")

print(miReq.status_code) #200 todo bien
print(miReq.headers) # Informacion de as.com en el header
print(miReq.text)#Texto de la pagina
print("--------------------------------------------------------")
print(miReq.content)#Texto de la pagina

docFinal=BeautifulSoup(miReq.text,"html.parser")

for i in docFinal.find_all("a"):
    
    print("Enlace: " , i['href'])
    
