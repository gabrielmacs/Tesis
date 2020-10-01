from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
from bson import ObjectId

#NYT
import nyt.apinewyorktimes as apinyt 
import nyt.noticianyt as nnyt
import json
import codecs
#NYT
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
  dataAT['ActoresTemas'] = []
  query=request.json['query']
  palabrasClaveRecibidas=request.json['palabrasClave']
  
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
  

  resumen=Resumen()
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
