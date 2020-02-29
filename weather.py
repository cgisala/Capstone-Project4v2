"""
This module uses the openweathermap api, process the response, and returns a list of the current weather description and average temperature
"""

import requests
from dataclasses import dataclass

""" Think about what data to return? """

def get_current_weather(city):
    """
    This function gets the city and gets the current weather data
    """    
    response = current_weather_api_call(city)
    list_forecasts  = process_current_weather_json(response)

    return list_forecasts

def current_weather_api_call(city):
    """
    Calls the call api server and gets the current weather data and returns dictionary of data
    """
    url = 'https://api.openweathermap.org/data/2.5/weather' 
    key = '931ff5eff05bb2caa4f58e70a64f78bb' #api key
    location = f'{city}, us'
    query = {'q': location, 'units':'imperial', 'appid': key} # formats the location, units, and API key into a dictionary

    return requests.get(url, params=query).json()


def process_current_weather_json(json):
    """
    Process the json and extract the current temp and weather description
    """
    today = Forecast(json['weather'][0]['description'], json['main']['temp'])
    return today


@dataclass
class Forecast:
    description: str 
    temp: float


