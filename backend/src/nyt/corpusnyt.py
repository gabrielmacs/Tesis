
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
paginanumero = 214
def get_news_elpais():
    
    # url definition
    url = "https://elpais.com/noticias/covid-19/"+str(paginanumero)
    
    # Request
    r1 = requests.get(url)
    r1.status_code

    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html5lib')

    # News identification
    coverpage_news = soup1.find_all('h2', class_='headline')
    
    print(len(coverpage_news))
    #print(type(len(coverpage_news)))
    number_of_articles = len(coverpage_news)
    #print(coverpage_news[0])

    # Empty lists for content, links and titles
    news_contents = []
    list_links = []
    list_date = []
    list_titles = []
    list_location = []

    for n in np.arange(0, number_of_articles):
        
        # only news articles (there are also albums and other things)
        if "album" in coverpage_news[n].find('a')['href']:  
            continue
        
        # Getting the link of the article
        link = coverpage_news[n].find('a')['href']
        #list_links.append(link)
        #print(list_links[0])

        # Getting the title
        title = coverpage_news[n].find('a').get_text()
        #list_titles.append(title)
        #print(list_titles[0])
        
        # Reading the content (it is divided in paragraphs)
        print("https://elpais.com"+link)
        article = requests.get("https://elpais.com"+link)
        print(article.status_code)

        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'html5lib')
        body = soup_article.find_all('div', class_='articulo-cuerpo')
        
        datosx =soup_article.find_all('div', class_='articulo-datos')
        #print(datosx)
        if(body):
            list_links.append(link)
            list_titles.append(title)
            if(datosx):
                if(datosx[0].find('span', class_='articulo-localizacion')):
                    lugar =datosx[0].find('span', class_='articulo-localizacion').get_text()
                    list_location.append(lugar)
                else:
                    list_location.append("Mundo")
                if(datosx[0].find('a').get_text()[0:12]):
                    fecha =datosx[0].find('a').get_text()[0:12]
                    list_date.append(fecha)
                
            
        print(len(body))
        
        if(body):
            x = body[0].find_all('p')

            # Unifying the paragraphs
            list_paragraphs = []
            for p in np.arange(0, len(x)):
                paragraph = x[p].get_text()
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)
            news_contents.append(final_article)

        
    print(len(news_contents))
    print(len(list_links))
    print(len(list_date))
    print(len(list_titles))
    print(len(list_location))      
    # df_features
    
    df_features = pd.DataFrame(
         {'Content': news_contents,
         'link': list_links
        })

    # df_show_info
    df_show_info = pd.DataFrame(
        {'Diario': 'El Pais',
         'Pais': list_location,
         'Fecha': list_date,
         'Noticia': list_titles,
         'Texto': news_contents,
         })
     
   
    return (df_features, df_show_info)
start = time.time()
x, y = get_news_elpais()
end =time.time()
te = end-start
print("The time elapsed is %f seconds" %(te))


print (x)
print (y)


# Create a Pandas Excel writer using XlsxWriter as the engine.
nombrepagina = "noticiaselpais"+str(paginanumero)+".xlsx"
writer = pd.ExcelWriter(nombrepagina, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
y.to_excel(writer, sheet_name='ElPais')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

print("Hoja numero: " + str(paginanumero))