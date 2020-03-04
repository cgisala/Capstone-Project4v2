"""
This module uses the openweathermap api, process the response, and returns a list of the current weather description and average temperature

*** To get the weather description and temperature call the 'get_current_weather' function ***

"""

import requests
from dataclasses import dataclass

""" Think about what data to return? """

def get_current_weather(city):
    """
    This function gets the city
    Returns the current weather condition and temperature
    """
    try:   
        response = current_weather_api_call(city)
        list_forecasts  = process_current_weather_json(response)

        return list_forecasts
    except:
        print('\nError: something broke\nTroubleshoot the weather.py')


def current_weather_api_call(city):
    """
    Calls the call api server and gets the current weather data and returns dictionary of data
    """

    url = 'https://api.openweathermap.org/data/2.5/weather' 
    key = '931ff5eff05bb2caa4f58e70a64f78bb' #api key is provided for convinience
    location = f'{city}, us' # city and country code

    """
    The parameters:
    Q is the city name and country code
    Units is imperial (Farenheit)
    """
    query = {'q': location, 'units':'imperial', 'appid': key} # formats the location, units, and API key into a dictionary

    response = requests.get(url, params=query).json() # the 'Get' request function returns a response object

    return response
  


def process_current_weather_json(json):
    """
    Process the json and extract the current temp and weather description
    """

    # Process the json and extracts the weather condition and current temperature
    today = Forecast(json['weather'][0]['description'], json['main']['temp'])

    return today


@dataclass
class Forecast:
    description: str 
    temp: float


