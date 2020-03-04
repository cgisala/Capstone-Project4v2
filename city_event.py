import search
import requests
from pprint import pprint
from requests import HTTPError

"""
get events for the city
"""

""" think about what data you will return """


def get_events(search_term, city):
    search_term, city = search
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
##def getInput():
###### return search_term, city
