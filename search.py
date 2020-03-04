"""
This module takes gets the city, makes three api calls, displays the information, and 
"""

import rest, weather, city_event, ui
import db

def search():

    # Calls the get city from the ui module and prompts the user to enter the city
    city = ui.get_city() 

    """
    The city variable is passed to the restaurant, events, and weather module to get the data from the server via API
    """
    restaurants = rest.get_restaurants(city) #Returns the restaurant in a particular city
    events = city_event.get_events(city) # Returns the events at the city
    current_weather = weather.get_current_weather(city) # Returns the weather condition and temp

    # The display function from the ui module takes in the restaurant data, events, and weather as arguments and displays the information
    ui.display(restaurants, events, current_weather)

    # figure out if user wants to save
    choice = input('Do you want to bookmark the results? y or n')
    choice = choice.lower() # Makes the choice case insensitive

    if choice == 'y':
        db.save(restaurants, events, weather)
    

    



