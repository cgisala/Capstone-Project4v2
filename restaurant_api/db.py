"""
save bookmark(data)
show all bookmark()
"""
from rest import Restaurant
from weather import Forecast
from datetime import datetime
import sqlite3
import os
conn = sqlite3.connect('Travel_app.sqlite')# create the database
cur = conn.cursor()
conn.execute('create table if not exists Travle_tip( Top_restaurants text, Top_news text, Top_weather text, Date_saved date)')
conn.execute('create table if not exists Restaurant ( Name text, Address text, Rating integer )')
conn.execute('create table if not exists Weather ( Description text, Tempreture float )')
# conn.execute('drop table Restaurant')# will drop table when needed
# conn.commit()




# Set up database 

""" first version: 4 columns:  top news story, top restaurant, some weather number, date saved.  

""" 

# think about table(s)

# def save(rest, news, weather):
#     # save these things to the database
#     pass
def save(rest, weather):
    #save method the restaurant that the user book-marked.
    rest = Restaurant("name", "address", 1) 
    row = conn.execute('insert into travel_tip(name, address, rating) values (?, ?, ?)', (rest.name, rest.address, rest.rating ))

    weather = Forecast("description", "temp")
    row = conn.execute('insert into weather(description, temp) values (?, ?)', (weather.description, weather.temp))
    conn.commit()
    return row.rowcount
   


# def get_all():
    # get all things, organize into list ?  and return 
#     return []

def get_all(city):
    rest_list = []
    city = input(" Enter city name: ")   
    get_all_sql = 'SELECT * FROM Restaurant WHERE city = ?'
    cur.execute(get_all_sql, (city, ))
    for row in cur.fetchall():
        rest_list.append(row)
    return rest_list

rows = conn.execute(get_all)
Restaurants = []
print([rows])
   

