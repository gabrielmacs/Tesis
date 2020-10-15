from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
from bson import ObjectId

#NYT
import nyt.apinewyorktimes as apinyt 
import nyt.noticianyt as nnyt
import json
import codecs
#NYT
#DOAJ
import doaj.apidoaj as apidoaj
import json
import codecs
#DOAJ
#El comercio
import elcomercio.apielcomercio as apicomercio
import elcomercio.corpuscomercio as ncomercio
import json
import codecs
#EL comercio
#procesamiento de textos
import json
import os
from collections import Counter
from Lematizacion.resumen import Resumen
#procesamiento de textos

#procesamiento de textos
nombreArchivoJSON = "ActoresTemas.json"
rutaActualpy = os.path.dirname(os.path.abspath(__file__))
pathArchivoJSON = os.path.join(rutaActualpy, nombreArchivoJSON)
dataAT = {}
dataAT['ActoresTemas'] = []
actoresTotales = []
temasTotales =[] 
palabrasClaveRecibidas=['casa', 'mesa']

#procesamiento de textos
#NYT
arreglolinksnoticias=[]
data ={} 
data['noticias']=[]
cantidad=1
#NYT


# Instantiation
app = Flask(__name__)
CORS(app, support_credentials=True)

# Settings


# Routes
@app.route('/autoresTemas', methods=['POST'])
def createUser():
  print(request.json)
  return request.json['name']


@app.route('/', methods=['POST', 'GET','OPTIONS'])
@cross_origin(supports_credentials=True)
def getUsers():
    return jsonify({"users":"asd"})


# New York Time
@app.route('/nyt', methods=['POST'])
@cross_origin(supports_credentials=True)
def obtenerNYT():   
  dataAT = {}
  arreglolinksnoticias=[]
  data ={} 
  dataAT['ActoresTemas'] = []
  query=request.json['query']
  data['noticias']=[]
  palabrasClaveRecibidas=request.json['palabrasClave']
  arreglolinksnoticias=[] 
  data ={} 
  data['noticias']=[]
  actoresTotales=[]
  temasTotales=[]
  c1=[]
  c2=[]

  print(request.json)
  with open('datanyt1.json','w', encoding='utf-8') as file:
      for n in range(cantidad):
          apinyt.execute(n,arreglolinksnoticias,query)
          for url in arreglolinksnoticias:  
              data['noticias'].append({'text':nnyt.get_news_nyt(url)})    
              #print(nnyt.get_news_nyt(url))    
      print(len(arreglolinksnoticias))
      json.dump(data,file,indent=4,ensure_ascii=False)
  print(request.json)
  

  resumen=Resumen("en")
  resumen.procesarPalabrasClave(palabrasClaveRecibidas)
  for i,noticia in enumerate(data['noticias']):
      print(i,"___________________________________________________________________")
      
      if (noticia['text']!=""):
          resumen.procesarTexto(noticia['text'])
   
      
          actoresTotales.extend(resumen.actoresStemming)

          temasTotales.extend(resumen.frasesDosPalabrasNoRepetidas)
          temasTotales.extend(resumen.frasesTresPalabras)
    

  c1=Counter(temasTotales).most_common(100)


    
  c2=Counter(actoresTotales).most_common(50)

  dataAT['ActoresTemas'].append({
  'Actores': c2,
  'Temas': c1
  })



  return dataAT


#FUENTES EN INGLES
#union de todas las feuntes en ingles
@app.route('/fuentesIngles', methods=['POST'])
@cross_origin(supports_credentials=True)
def obtenerFuentesIngles():   
 

  dataAT = {}
  arreglolinksnoticias=[]
  data ={} 
  dataAT['ActoresTemas'] = []
  query=request.json['query']
  palabrasClaveRecibidas=request.json['palabrasClave']
  arreglolinksnoticias=[] 
  data ={} 
  data['noticias']=[]
  actoresTotales=[]
  temasTotales=[]
  c1=[]
  c2=[]

  if(request.json['nyt']=='true'):
    with open('datanyt1.json','w', encoding='utf-8') as file:
        for n in range(cantidad):
            apinyt.execute(n,arreglolinksnoticias,query)
            for url in arreglolinksnoticias:  
                data['noticias'].append({'text':nnyt.get_news_nyt(url)})    
                #print(nnyt.get_news_nyt(url))    
        print(len(arreglolinksnoticias))
        json.dump(data,file,indent=4,ensure_ascii=False)
  print(request.json)
  

  if(request.json['doaj']=='true'):
    with open('datadoaj.json','w', encoding='utf-8') as file:
          for n in range(cantidad):  
              apidoaj.execute(n,apidoaj.arregloarticulos,query) 
          data['noticias'].extend(apidoaj.data["datadoaj"])
          json.dump(data['noticias'],file,indent=4,ensure_ascii=False) 

  print(data['noticias'])
  resumen=Resumen("en")
  resumen.procesarPalabrasClave(palabrasClaveRecibidas)
  for i,noticia in enumerate(data['noticias']):
      print(i,"___________________________________________________________________")
      
      if (noticia['text']!=""):
          resumen.procesarTexto(noticia['text'])
   
      
          actoresTotales.extend(resumen.actoresStemming)

          temasTotales.extend(resumen.frasesDosPalabrasNoRepetidas)
          temasTotales.extend(resumen.frasesTresPalabras)
    

  c1=Counter(temasTotales).most_common(100)


    
  c2=Counter(actoresTotales).most_common(50)

  dataAT['ActoresTemas'].append({
  'Actores': c2,
  'Temas': c1
  })



  return dataAT





# DOAJ
@app.route('/doaj', methods=['POST'])
@cross_origin(supports_credentials=True)
def obtenerDOAJ():   
  data ={} 
  data['noticias']=[]
  dataAT = {}
  dataAT['ActoresTemas'] = []
  data['noticias']=[]
  query=request.json['query']
  palabrasClaveRecibidas=request.json['palabrasClave']
  actoresTotales=[]
  temasTotales=[]
  c1=[]
  c2=[]
  print(request.json)
  with open('datadoaj.json','w', encoding='utf-8') as file:
        for n in range(cantidad+1):  
            apidoaj.execute(n,apidoaj.arregloarticulos,query) 
        data['noticias']= apidoaj.data["datadoaj"]
        json.dump(apidoaj.data,file,indent=4,ensure_ascii=False) 
  
  print(data['noticias'])

  resumen=Resumen("en")
  resumen.procesarPalabrasClave(palabrasClaveRecibidas)
  for i,noticia in enumerate(data['noticias']):
      print(i,"___________________________________________________________________")
      
      if (noticia['text']!=[]):
          resumen.procesarTexto(noticia['text'])
   
      
          actoresTotales.extend(resumen.actoresStemming)

          temasTotales.extend(resumen.frasesDosPalabrasNoRepetidas)
          temasTotales.extend(resumen.frasesTresPalabras)
    

  c1=Counter(temasTotales).most_common(100)


    
  c2=Counter(actoresTotales).most_common(50)

  dataAT['ActoresTemas'].append({
  'Actores': c2,
  'Temas': c1
  })



  return dataAT


# El Comercio
@app.route('/comercio', methods=['POST'])
@cross_origin(supports_credentials=True)
def obtenerComercio():
  data ={} 
  data['noticias']=[]
  dataAT = {}
  dataAT['ActoresTemas'] = []
  data['noticias']=[]
  query=request.json['query']
  palabrasClaveRecibidas=request.json['palabrasClave']
  actoresTotales=[]
  temasTotales=[]
  c1=[]
  c2=[]
  arreglolinksnoticias=[]


  print(request.json)


  with open('dataelcomercio.json','w', encoding='utf-8') as file:
    for n in range(cantidad +3):
        apicomercio.execute(n,arreglolinksnoticias,query)
        for url in arreglolinksnoticias:
            data['noticias'].append({'text':[ncomercio.get_news_elcomercio(url)]})    
            #print(nnyt.get_news_nyt(url))    
            #print(len(arreglolinksnoticias))
    json.dump(data,file,indent=4,ensure_ascii=False)


  resumen=Resumen("es")
  resumen.procesarPalabrasClave(palabrasClaveRecibidas)
  for i,noticia in enumerate(data['noticias']):
      print(i,"___________________________________________________________________")
      
      if (noticia['text']!=[]):
          resumen.procesarTexto(noticia['text'][0])
   
      
          actoresTotales.extend(resumen.actoresStemming)

          temasTotales.extend(resumen.frasesDosPalabrasNoRepetidas)
          temasTotales.extend(resumen.frasesTresPalabras)
    

  c1=Counter(temasTotales).most_common(100)


    
  c2=Counter(actoresTotales).most_common(50)

  dataAT['ActoresTemas'].append({
  'Actores': c2,
  'Temas': c1
  })



  return dataAT


if __name__ == "__main__":
    app.run(debug=True)



