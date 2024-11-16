from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import csv

class PostCrawler():
    
    def __init__(self,titulo,emoticono,contenido):
        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido

    def __str__(self) -> str:
        return "Titulo: " + str(self.titulo) + " Emoticono: " + str(self.emoticono) + " Contenido: " + str(self.contenido)

class ExtraerInformacion():
    
    def extraeInfo(self):
        urlBase="https://python.beispiel.programmierenlernen.io/index.php"
        miDoc=requests.get("https://python.beispiel.programmierenlernen.io/index.php")

        
        #Para el programa durante dos segundos  para que no se hagan muchas en poco tiempo
        time.sleep(2)
        docFinal=BeautifulSoup(miDoc.text,"html.parser")

        titulo=docFinal.select(".card-title")
        tecto=docFinal.select(".card-text")
        listaEmoji=docFinal.select(".emoji")
        listaimagenes=docFinal.select("img")
        lista=[]
        print(urljoin(urlBase,listaimagenes[0].attrs["src"]))
        for i in range(0,5):
            post=PostCrawler(titulo[i].text,listaEmoji[i].text,tecto[i].text)
            
            lista.append(post)
        
        web2=docFinal.select_one(".navigation .btn").attrs["href"]
        print(urljoin(urlBase,web2))    
        
        return lista

extrae=ExtraerInformacion()

lista=extrae.extraeInfo()


with open('crawler.csv', 'w', newline='', encoding="utf-8") as csvfile:
    for i in lista:
        spamwriter = csv.writer(csvfile, delimiter=';',#Excel ; es delikmitador de columna
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([i.emoticono , i.contenido])
    
for i in lista:
    print(i)
            