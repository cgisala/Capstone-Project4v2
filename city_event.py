"""
get events for the city
"""

""" think about what data you will return """

import requests
from pprint import pprint
from requests import HTTPError


def get_events():
    search_term, city = getInput()
    query = {'keyword': search_term, 'location': city}

    # Exception handler
    try:
        url = 'http://api.eventful.com/json/events/search?&app_key=bgw8NQ28vRcNxKHB'
        data = requests.get(url, params=query).json()
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')

    except Exception as ex:
        print(f'Other error: {ex}')

    else:
        return data

    get_events()


# user input
def getInput():
    search_term = input("Enter event keywords you are looking for : ")
    city = input("Enter the city name :  ")

    return search_term, city
