import apinewyorktimes as apinyt 
import noticianyt as nnyt
import json
import codecs


arreglolinksnoticias=[]
data ={} 
data['noticias']=[]
cantidad=2
query="skype"

    
with open('datanyt1.json','w', encoding='utf-8') as file:
    for n in range(cantidad):
        apinyt.execute(n,arreglolinksnoticias,query)
        for url in arreglolinksnoticias:
            data['noticias'].append({'text':nnyt.get_news_nyt(url)})    
            #print(nnyt.get_news_nyt(url))    
    print(len(arreglolinksnoticias))
    json.dump(data,file,indent=4,ensure_ascii=False)


    