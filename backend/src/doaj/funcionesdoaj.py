import apidoaj as apidoaj
import json
import codecs

cantidad=5
query="Cama"
idioma= "ES"

'''
with open('datadoaj.json','w', encoding='utf-8') as file:
    for n in range(cantidad):
        apidoaj.execute(n,arregloarticulos,query)
        print(str(n)+":     "+arregloarticulos[0]['abstract'])
        data['datadoaj'].append({'text': arregloarticulos[n]['abstract']})    
            #print(nnyt.get_news_nyt(url))    
        json.dump(data,file,indent=4,ensure_ascii=False)
    print(len(arregloarticulos))
'''
 #execute(1,arregloarticulos,"Shadow")
with open('datadoajx.json','w', encoding='utf-8') as file:
    for n in range(cantidad): 
       
        apidoaj.execute(n,apidoaj.arregloarticulos,query,"EN")  
        apidoaj.arregloarticulos = []
    json.dump(apidoaj.data,file,indent=4,ensure_ascii=False)  
  #print(nnyt.get_news_nyt(url))    


