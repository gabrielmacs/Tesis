import apidoaj as apidoaj
import json
import codecs

#cantidad=1
query="Hydrostatic"
idioma= "EN"

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
#print(apidoaj.cantidadarticulos(1,query)) 
'''for n in range(1,apidoaj.cantidadarticulos(1,query,idioma)):       
    apidoaj.execute(n,query,idioma)  
'''
if(apidoaj.cantidadarticulos2(1,query,idioma)>20):
    for n in range(1,apidoaj.cantidadpagina(1,query,idioma)):       
        apidoaj.execute(n,query,idioma,"asc")  
    for m in range(1,apidoaj.cantidadpagina(1,query,idioma)):       
        apidoaj.execute(m,query,idioma,"desc")
else:
    for m in range(1,apidoaj.cantidadpagina(1,query,idioma)):       
        apidoaj.execute(m,query,idioma,"desc")
with open('datadoajx.json','w', encoding='utf-8') as file:
    
    json.dump(apidoaj.data,file,indent=4,ensure_ascii=False)  
  #print(nnyt.get_news_nyt(url))    


    