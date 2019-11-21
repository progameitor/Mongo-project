import requests
import os 
import json 
from dotenv import load_dotenv

load_dotenv()
YELP_API_KEY = os.getenv("YELP_API_KEY")
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}

ciudades= {"es_ES":["Madrid","Barcelona","Sevilla","Valencia"]}
codes= ["cs_CZ","da_DK","de_AT","de_CH","de_DE","en_AU","en_BE","en_CA","en_CH","en_GB","en_HK","en_IE","en_MY","en_NZ","en_PH","en_SG","en_US","es_AR","es_CL","es_ES","es_MX","fi_FI","fil_PH",
"fr_BE","fr_CA","fr_CH","fr_FR","it_CH","it_IT","ja_JP","ms_MY","nb_NO","nl_BE","nl_NL","pl_PL","pt_BR","pt_PT","sv_FI","sv_SE","tr_TR","zh_HK","zh_TW"]

for key,value in ciudades.items():
    if 


def get_apis(company):
    param_list = []
    for i in codes:
        param_list.append([{'term': company,
            'location' : "en_US",
            'limit' : 50,
            'locale': i,}])
    return param_list


reponse=[]
def get_request():
    for i in get_apis("Starbucks"):
        requests.get(url = ENDPOINT, params = i, headers = HEADERS)

          #poner un time punto sleep


    return None

print(get_request())    
   
       






           
    


       
       
       

    
  


  
           
        

        

   




    







