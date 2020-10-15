# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# http://docs.python-requests.org/en/master/user/install/
import time
import requests
import re
import json
import codecs
arregloarticulos=[]
data ={} 
data['datadoaj']=[]
#cantidad=10
#query="Energia"

def execute(a,arregloarticulos,query,idioma):
  print(query)
  print(re.sub(" ","%20",query))
  queryf=re.sub(" ","%20",query)
  paginabusqueda=str(a)  
  print("********************Numero de pagina"+str(a)) 
  requestUrl = "https://doaj.org/api/v1/search/articles/(title%3A%22"+queryf+"%22)%20OR%20(bibjson.abstract%3A%22"+queryf+"%22)?page="+paginabusqueda+"&pageSize=100"
  print(requestUrl)
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  print(request.status_code)
  #print(request.json())
  
  if(request.status_code==200):
    respuestajson =request.json()
    print("total archivos "+str(respuestajson['total']))
    if(respuestajson['total']>0):
      noticiasjson=respuestajson['results']
      #print(noticiasjson[0])
      
      for documento in noticiasjson:
          articulo = documento['bibjson']
          metaarticulo = articulo['journal']
          arregloarticulos.append(articulo)  
          #print(documento['bibjson'])
          if('abstract' in articulo  ):
            #and 'EN' in articulo['language']
            if( idioma in metaarticulo['language']):
              #i = i + 1
              #print(metaarticulo['language'])
              data['datadoaj'].append({'text': articulo['abstract']})
              
            
            #arregloarticulos.pop()  
          
    else:
      print("No se encontro resultados")  
  print(len(arregloarticulos))
  #print(arregloarticulos[1]['abstract'])
 

'''
#execute(1,arregloarticulos,"Shadow")
with open('datadoaj.json','w', encoding='utf-8') as file:
    for n in range(cantidad):  
        execute(n,arregloarticulos,query)  
    json.dump(data,file,indent=4,ensure_ascii=False)  
  #print(nnyt.get_news_nyt(url))    
'''