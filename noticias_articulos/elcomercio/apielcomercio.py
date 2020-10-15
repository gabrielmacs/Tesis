# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# http://docs.python-requests.org/en/master/user/install/
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import re
arreglolinksnoticias=[]

def execute(a,arreglolinksnoticias,query):
  print(query)
  print(re.sub(" ","+",query))
  queryf=re.sub(" ","+",query)
  paginabusqueda=str(a)  
  requestUrl = "https://www.elcomercio.com/search/"+paginabusqueda+"?query="+queryf+"&_type=all&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&contentTypes%5B%5D=news"
  # Request
  r1 = requests.get(requestUrl)
  r1.status_code

  # We'll save in coverpage the cover page content
  coverpage = r1.content

  # Soup creation
  soup1 = BeautifulSoup(coverpage, 'html5lib')

  # News identification
  coverpage_news = soup1.find_all('div', class_='article')
    
  print(len(coverpage_news))
  #print(type(len(coverpage_news)))
  number_of_articles = len(coverpage_news)
  #print(coverpage_news[0])
  for n in np.arange(0, number_of_articles):
     arreglolinksnoticias.append("https://www.elcomercio.com"+coverpage_news[n].find('a')['href'])  
  #print(arreglolinksnoticias)  
  
#execute(0,arreglolinksnoticias,"Covid Ecuador")  
  