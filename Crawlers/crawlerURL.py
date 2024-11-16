from bs4 import BeautifulSoup
import requests

miDoc=requests.get("https://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text,"html.parser")