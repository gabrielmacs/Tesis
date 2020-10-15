

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import json
def get_news_nyt(url):
    # url definition
    #url = "https://www.nytimes.com/2020/07/21/business/economy/coronavirus-cities.html"
    # Request
    article = requests.get(url)
    print(article.status_code)

    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('section', class_='meteredContent')
    news_contents=''
    if(body):
        print("Rasgando texto...")
        x = body[0].find_all('p')

        # Unifying the paragraphs
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = "".join(list_paragraphs)
           
        news_contents=final_article
# df_show_info
    
    return (news_contents)
#y = get_news_nyt()
#print (y)

#data ={} 
#data['noticias']=[]
#data['noticias'].append({'text':get_news_nyt("https://www.nytimes.com/2020/07/21/business/economy/coronavirus-cities.html")})    
#with open('datanyt1.json','w') as file:
#    json.dump(data,file,indent=4)