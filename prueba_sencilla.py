import requests
import os 
import json 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
YELP_API_KEY = os.getenv("YELP_API_KEY")
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}


def obtenerTodo(company,city):
    
    
    PARAMS =({'term': company,
            'location': city,
            'limit': 50})


    response =requests.get(url = ENDPOINT, params = PARAMS, headers = HEADERS)

    api_query=json.loads(response.text) 
        
        
    coords = []
    names = []
    city = []
    
    yelp_dict = {}
    coords_list = []
    coords_2 = []

    
    
    for i in api_query["businesses"]:
        coords.append(i["coordinates"])
        names.append(i["name"])
        city.append(i["location"]["city"])
        

    for i in coords:
        coords_list.append([i["longitude"], i["latitude"]])

    for i in range(len(coords_list)):
        longitude = coords_list[i][0]
        latitude = coords_list[i][1]
        coords_2.append({"Type":"Point", "coordinates":[longitude,latitude]})
        
    yelp_dict = {"Name":names,"City":city,"Coordinates":coords_list,"Geometry":coords_2}

    return pd.DataFrame(yelp_dict)

    