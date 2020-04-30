

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time

# url 
url = "https://www.eluniverso.com/tema/coronavirus-wuhan"
# Request
r1 = requests.get(url)
print(r1.status_code)

#se necesita un estado 200
# Aqui esta pagania su contenido
coverpage = r1.content


soup1 = BeautifulSoup(coverpage, 'html5lib')

# Buscar la parte de la notica 
coverpage_news = soup1.find_all('div', class_='articulo-contenido')
print(len(coverpage_news))
print(coverpage_news[4])
