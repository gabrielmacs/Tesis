import apinewyorktimes as apinyt 
import noticianyt as nnyt
import json
import codecs


class funcionesNYT  :
    arreglolinksnoticias=[]
    data ={} 
    data['noticias']=[]
    cantidad=1


    def __init__(self,query):
        with open('datanyt1.json','w', encoding='utf-8') as file:
            for n in range(self.cantidad):
                apinyt.execute(n,self.arreglolinksnoticias,query)
                for url in self.arreglolinksnoticias:
                    self.data['noticias'].append({'text':nnyt.get_news_nyt(url)})    
                    #print(nnyt.get_news_nyt(url))    
            print(len(self.arreglolinksnoticias))
            json.dump(self.data,file,indent=4,ensure_ascii=False)


    