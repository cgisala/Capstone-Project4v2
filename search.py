"""
1. get city
2. make 3 api calls.
3. display results
"""

import rest, weather, city_event
import db
import ui


def search():

    city = ui.get_city()
    restaurants = rest.get_restaurants(city)
    events = city_event.get_events(city)
    weather_forecast = weather.get_forecast(city)

    ui.display(restaurants, events)

    # figure out if user wants to save

    if user_wants_to_save:
        db.save(restaurants, events, weather_forecast)

    



