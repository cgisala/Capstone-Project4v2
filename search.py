"""
1. get city
2. make 3 api calls.
3. display results
"""

import rest, weather, news
import db

def search():

    city = ui.get_city()
    restaurants = rest.get_restaurants(city)
    news_articles = news.get_articles(city)
    weather_forecast = weather.get_forecast(city)

    ui.display(restaurants, news_articles, weather_forecast)

    # figure out if user wants to save

    if user_wants_to_save:
        db.save(restaurants, news_articles, weather_forecast)

    



