# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# http://docs.python-requests.org/en/master/user/install/
import time
import requests
import re
import json
import codecs
data ={} 
data['datadoaj']=[]
#cantidad=10
#query="Energia"

def execute(a,query,idioma,orden):
  #data['datadoaj']=[]
  print(query)
  print(re.sub(" ","%20",query))
  queryf=re.sub(" ","%20",query)
  paginabusqueda=str(a)  
  print("********************Numero de pagina"+str(a)) 
  requestUrl = "https://doaj.org/api/v1/search/articles/(title%3A%22"+queryf+"%22)%20OR%20(bibjson.abstract%3A%22"+queryf+"%22)%20AND%20(bibjson.journal.language%3A%22"+idioma+"%22)?page="+paginabusqueda+"&pageSize=100&sort=year%3A"+orden
  print(requestUrl)
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  print(request.status_code)
  #print(request.json())
  
  if(request.status_code==200):
    respuestajson =request.json()
    if(respuestajson['total']!=0):
      noticiasjson=respuestajson['results']
      
      #print(noticiasjson[0])
      for documento in noticiasjson:
          articulo = documento['bibjson']
          #metaarticulo = articulo['journal']
         
          #print(documento['bibjson'])
          if('abstract' in articulo):
            #and 'EN' in articulo['language']
            #if( idioma in metaarticulo['language']):
            #i = i + 1
            #print(metaarticulo['language'])
            data['datadoaj'].append({'text': articulo['abstract']})
            #print(articulo['abstract'])  
            
            #arregloarticulos.pop()  
          
    else:
      print("No se encontro resultados")  
  
  #print(arregloarticulos[1]['abstract'])
def cantidadpagina(a,query,idioma):
  queryf=re.sub(" ","%20",query)
  paginabusqueda=str(a)  
  requestUrl = "https://doaj.org/api/v1/search/articles/(title%3A%22"+queryf+"%22)%20OR%20(bibjson.abstract%3A%22"+queryf+"%22)%20AND%20(bibjson.journal.language%3A%22"+idioma+"%22)?page="+paginabusqueda+"&pageSize=100"
  #"http://api.springernature.com/meta/v2/json?q=(title%3A%22"+queryf+"%22%20OR%20keyword%3A%22"+queryf+"%22)&p=100&s="+paginabusqueda+"&api_key=3baefd29b9ce65a833af4889a0cacbed"
  #print(requestUrl)
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  #print(request.json())
  
  if(request.status_code==200):
    respuestajson =request.json()
    print("total archivos "+str(respuestajson['total']))
    
    if(((respuestajson['total']//100)+1)>10):
      numarticulo = 11
    else:
      numarticulo = (respuestajson['total']//100)+2  
      
  return (numarticulo)

def cantidadarticulos2(a,query,idioma):
  queryf=re.sub(" ","%20",query)
  paginabusqueda=str(a)  
  requestUrl = "https://doaj.org/api/v1/search/articles/(title%3A%22"+queryf+"%22)%20OR%20(bibjson.abstract%3A%22"+queryf+"%22)%20AND%20(bibjson.journal.language%3A%22"+idioma+"%22)?page="+paginabusqueda+"&pageSize=100"
  #"http://api.springernature.com/meta/v2/json?q=(title%3A%22"+queryf+"%22%20OR%20keyword%3A%22"+queryf+"%22)&p=100&s="+paginabusqueda+"&api_key=3baefd29b9ce65a833af4889a0cacbed"
  #print(requestUrl)
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  #print(request.json())
  
  if(request.status_code==200):
    respuestajson =request.json()
    print("total archivos "+str(respuestajson['total']))       
    numarticulo = (respuestajson['total']//100)+2  
      
  return (numarticulo)
'''
#execute(1,arregloarticulos,"Shadow")
with open('datadoaj.json','w', encoding='utf-8') as file:
    for n in range(cantidad):  
        execute(n,arregloarticulos,query)  
    json.dump(data,file,indent=4,ensure_ascii=False)  
  #print(nnyt.get_news_nyt(url))    
'''