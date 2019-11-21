import requests
import os 
import json 
from dotenv import load_dotenv

load_dotenv()
YELP_API_KEY = os.getenv("YELP_API_KEY")
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % YELP_API_KEY}


#DEfine parametrers
PARAMETERS = {'term': 'school'}
              
              
              'location': 'San Francisco'}  



response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

business_data = response.json()

print(business_data)