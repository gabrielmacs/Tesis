import apinewyorktimes as apinyt 
import noticianyt as nnyt
import json
import codecs
import time
arreglolinksnoticias=[]
data ={} 
data['noticias']=[]
cantidad=25
query="Covid"
with open('datanytpaul.json','w', encoding='utf-8') as file:
    for n in range(cantidad):
         
        
        apinyt.execute(n,arreglolinksnoticias,query)
        #time.sleep(6)
        for url in arreglolinksnoticias:
            data['noticias'].append({'text':nnyt.get_news_nyt(url)})    
            #print(nnyt.get_news_nyt(url))    
        arreglolinksnoticias=[]
    print(len(arreglolinksnoticias))
    json.dump(data,file,indent=4,ensure_ascii=False)


    