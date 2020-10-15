import apielcomercio as apicomercio
import corpuscomercio as ncomercio
import json
import codecs
arreglolinksnoticias=[]
data ={} 
data['noticias']=[]
cantidad=2
#el numero de paginas a buscar cada una tiene 20 noticias
query="covid"
with open('dataelcomercio.json','w', encoding='utf-8') as file:
    for n in range(cantidad):
        apicomercio.execute(n,arreglolinksnoticias,query)
        for url in arreglolinksnoticias:
            data['noticias'].append({'text':ncomercio.get_news_elcomercio(url)})    
            #print(nnyt.get_news_nyt(url))    
            #print(len(arreglolinksnoticias))
    json.dump(data,file,indent=4,ensure_ascii=False)