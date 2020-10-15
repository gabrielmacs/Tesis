# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# http://docs.python-requests.org/en/master/user/install/
import time
import requests
import re
arreglolinksnoticias=[]
def execute(a,arreglolinksnoticias,query):
  print(query)
  print(re.sub(" ","%20",query))
  queryf=re.sub(" ","%20",query)
  keyapi="AxK7SoEikjMo0eKbtXMN9Rc18BJjtDTA"
  paginabusqueda=str(a)  
  requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=The%20New%20York%20Times&page="+paginabusqueda+"&q="+queryf+"&fl=web_url&api-key="+keyapi
  requestHeaders = {
    "Accept": "application/json"
  }

  request = requests.get(requestUrl, headers=requestHeaders)
  #print(request.status_code)
  #print(request.json())
  
  if(request.status_code==200):
    #time.sleep(6)  
    respuestajson =request.json()
    noticiasjson=respuestajson['response']
    for documento in noticiasjson['docs']:
        arreglolinksnoticias.append(documento['web_url'])  
    #print(arreglolinksnoticias)  
  print(len(arreglolinksnoticias))

  
  