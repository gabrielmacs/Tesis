

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import json
def get_news_elcomercio(url):
    # url definition
    #url = "https://www.elcomercio.com/deportes/independiente-sello-espanol-futbol-femenino.html"
    # Request
    article = requests.get(url)
    print(article.status_code)

    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='paragraphs')
    news_contents = []
    #print(body)
    if(body):
        
        print("Rasgando texto...")
        x = body[0].find_all('p')

        # Unifying the paragraphs
        list_paragraphs = []
        a =len(x)
        if body[0].find('blockquote', class_='twitter-tweet'):
            a =len(x)-1
        for p in np.arange(a):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)             
        #print(final_article)   
        news_contents=final_article
# df_show_info
    
    return (news_contents)
#y = get_news_elcomercio()


#data ={} 
#data['noticias']=[]
#data['noticias'].append({'text':get_news_nyt("https://www.nytimes.com/2020/07/21/business/economy/coronavirus-cities.html")})    
#with open('datanyt1.json','w') as file:
#    json.dump(data,file,indent=4)