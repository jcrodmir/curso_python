from bs4 import BeautifulSoup
import requests

miDoc=requests.get("https://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text,"html.parser")

titulo=docFinal.select(".card-title")
tecto=docFinal.select(".card-text")
listaEmoji=docFinal.select(".emoji")

for i in range(0,5):
    print("\n -------CARD------")
    print(titulo[i].text)
    print(tecto[i].text)
    

