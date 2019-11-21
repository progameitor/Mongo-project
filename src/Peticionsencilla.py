import requests
import os 
import json 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
YELP_API_KEY = os.getenv("YELP_API_KEY")
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}

PARAMS =({'term': "airport",
            'location': "seattle",
            'limit': 50})


response =requests.get(url = ENDPOINT, params = PARAMS, headers = HEADERS)
print(response.text)