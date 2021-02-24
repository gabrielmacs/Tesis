
import time
import requests
import re
import json
import codecs
arregloarticulos=[]
#cantidad=10
#query="Energia"
data ={} 
data['dataspringer']=[]
def execute(a,query):
  ##agregaresto
  #data['dataspringer']=[]
  respuestajson = []
  arregloarticulos=[]
  articulosjson= []
  print(query)
  print(re.sub(" ","%20",query))
  queryf=re.sub(" ","%20",query)
  r = (a * 100 + 1)
  paginabusqueda=str(r)  

  print("********************Numero de pagina"+str(a)) 
  requestUrl = "http://api.springernature.com/meta/v2/json?q=(title%3A%22"+queryf+"%22%20OR%20keyword%3A%22"+queryf+"%22)&p=100&s="+paginabusqueda+"&api_key=3baefd29b9ce65a833af4889a0cacbed"
  #"http://api.springernature.com/meta/v2/json?q=(title%3A%22"+queryf+"%22%20OR%20keyword%3A%22"+queryf+"%22)&p=100&s="+paginabusqueda+"&api_key=3baefd29b9ce65a833af4889a0cacbed"
  print(requestUrl)
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  print(request.status_code)
  #print(request.json())
  
  if(request.status_code==200):
    respuestajson =request.json()
    
    numarticulo = respuestajson['result']
    numerito =numarticulo[0]
    print("total archivos "+numerito['total'])
    print(((int(numerito['total']))//100)+1)
    if((int(numerito['total']))>0):
      #print("total archivos "+str(numarticulo['total']))
      articulosjson=respuestajson['records']
      #print(noticiasjson[0])
      
      for documento in articulosjson:
          arregloarticulos.append(documento)  
          #print(documento['bibjson'])
          if('abstract' in documento):
            data['dataspringer'].append({'text': documento['abstract']})
            #arregloarticulos.pop()  
          
    else:
      print("No se encontro resultados")  
  print(len(arregloarticulos))
  #print(arregloarticulos[1]['abstract'])
  request.close()
def cantidadarticulos(query):
  limite = 5000
  print(query)
  print(re.sub(" ","%20",query))
  queryf=re.sub(" ","%20",query)
  
  requestUrl = "http://api.springernature.com/meta/v2/json?q=(title%3A%22"+queryf+"%22%20OR%20keyword%3A%22"+queryf+"%22)&p=0&s=0&api_key=3baefd29b9ce65a833af4889a0cacbed"
  #"http://api.springernature.com/meta/v2/json?q=(title%3A%22"+queryf+"%22%20OR%20keyword%3A%22"+queryf+"%22)&p=100&s="+paginabusqueda+"&api_key=3baefd29b9ce65a833af4889a0cacbed"
  print(requestUrl)
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  print(request.status_code)
  #print(request.json())
  
  if(request.status_code==200):
    respuestajson =request.json()
    numarticulo = respuestajson['result']
    numerito =numarticulo[0]
    numeritopagina =(int(numerito['total']))
    if(numeritopagina <= limite):
      numeritoaux = numeritopagina
    else:
      numeritoaux =  limite
    
  else:
    numeritoaux = 0
    print("No se encontro resultados") 
     
  
  return (((numeritoaux)//100)+1)  

