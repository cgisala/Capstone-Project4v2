"""
get weather for the city
"""

from dataclasses import dataclass

""" Think about what data to return? """

def get_forecast(city):
    
    # make api call
    # make Forecast objects 
    # return list of Forecast objects

    response = make_api_call(city)

    list_forecasts  = process_json(response)

    return list_forecasts


def make_api_call(city):
    # fill in here 
    return {}   


def process_json(json):

    # use actual data from json
    today = Forecast('sunshine', 30)
    tomorrow = Forecast('cloudy', 23)
    return [today, tomorrow]


@dataclass
class Forecast:
    description: str 
    temp: float


