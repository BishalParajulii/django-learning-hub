import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://phoneintelligence.abstractapi.com/v1/"

def fetch_phone_number(phone:str , country='NP'):
    url = BASE_URL
    
    params = {
        "api_key" : os.getenv("PHONE_API_KEY"),
        "phone" : phone,
        "country" : country
    }
    
    response = requests.get(url , params=params)
    return response.json()
    