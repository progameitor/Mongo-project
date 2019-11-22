        
import requests
import os 
import json 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
YELP_API_KEY = os.getenv("YELP_API_KEY")
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}


def obtenerMejor(company,city):
    
    
    PARAMS =({'term': company,
            'location': city,
            'limit': 50})


    response =requests.get(url = ENDPOINT, params = PARAMS, headers = HEADERS)

    api_query=json.loads(response.text) 
        
        
    lat = []
    names = []
    city = []
    
    yelp_dict = {}
    
    for i in api_query["businesses"]:
        lat.append(api_query["businesses"][i]["coordinates"]["latitude"])
        names.append(i["name"])
        city.append(i["location"]["city"])
        

   
        
    yelp_dict = {"Name":names,"City":city,"latitud":lat}

    return pd.DataFrame(yelp_dict)