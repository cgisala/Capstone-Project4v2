#from search import *
import requests
from weather import Forecast
import db
import os

#Restaurant class and its atributes are created
class Restaurant():
    def __init__(self, name, address, rating):
        self.name = name
        self.address = address
        self.rating = rating
   
RESTAURANT_KEY = os.environ.get('RESTAURANT_KEY')
url ='https://api.yelp.com/v3/businesses/search'

"""
get restaurant for the city
""" 
#get the restaurant info put it into the list    
def get_restaurants():
    name_info = []
    address_info =[]
    rating_info = []
    query = input('What kind of restaurant? ')
    headers = {'Authorization': 'Bearer ' + RESTAURANT_KEY}
    params = {'term': query, 'categories': 'restaurants', 'location': 'Minneapolis,MN', 'radius': '10000', 'price': 1, 'limit': 10}
    response = requests.get(url, headers=headers, params=params).json()
    #print(response)


    restaurants = response['businesses']

    for i in restaurants:
        name = i['name']
        location = i['location']
        address = ' , '.join(location['display_address'])
        rating = i['rating']
        #print(f'{name}, {address}, {rating}')
        name_info.append(name)
        address_info.append(address)
        rating_info.append(rating)
    return name_info, address_info, rating_info


    #return "caribou coffee"
    # todo make api call 
 #loop through and pring in list   
r_name, r_address, r_rating = get_restaurants()
for r in range(len(r_name)):
    print(f'{r_name[r]} {r_address[r]} {r_rating[r]} ')
