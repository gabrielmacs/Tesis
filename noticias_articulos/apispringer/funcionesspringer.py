import apispringer as apispringer
import json
import codecs


query="Soon"
cantidad=apispringer.cantidadarticulos(1,query)


for n in range(cantidad): 
    #apispringer.arregloarticulos = []
    apispringer.execute(n,query)  
with open('dataspring.json','w', encoding='utf-8') as file:
   json.dump(apispringer.data,file,indent=4,ensure_ascii=False)  
  #print(nnyt.get_news_nyt(url))    


    