
import city_event
import eventObj
import db
import  city_event ,rest ,weather

"""
def show menu
def get search term
def display(weather, events, restaurants)
"""


def show_menu(self):
    while True:
        choice = (input("*****MENU***** \n: quit \n:""search \n: show \n"))
        if choice == 'quit':
            break
        elif choice == 'search':
            self.get_search_term()
        elif choice == 'show':
            self.show()

        else:
            if choice != 'quit' and choice != 'search' and choice != 'show':
                print('you have to enter :  quit/search/show')


def get_search_term(search_term, city):
    weather_response = weather.get_current_weather(search_term)
    restaurant_response = rest.get_restaurants(search_term)
    event_response = city_event.get_events(search_term, city)
    return weather_response, restaurant_response, event_response


def show():
    all_data = db.get_all()
    print(all_data)


# def display(weather, restaurant, events):