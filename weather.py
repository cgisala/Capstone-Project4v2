import requests
from datetime import datetime

key = '931ff5eff05bb2caa4f58e70a64f78bb'
url = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    """
    This function gets takes in the city and get the weather data from the server specific to the city.
    """
    location = f'{city},us'  # city and country
    query = {'q': location, 'units':'imperial', 'appid': key} # formats the location, units, and API key into a dictionary
    api_data = api_connection(url, query)
    weather_data = object_empty(api_data)
    
    return weather_data

def api_connection(url, query):
    """
    Checks if able to connect to the API server and if not returns an error message
    """
    try:
        data = requests.get(url, params=query).json()
        return data
    except:
        print('Error - unable to connect to the API server')

def object_empty(data):
    """
    Checks to see if weather data is empty
    """
    if data is None:
        print('Error - there is no data in the object')
    else:
        return data