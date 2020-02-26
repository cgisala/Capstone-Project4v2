"""
1. call method to Displays menu
2. def search city
3. def view calls saved data from the database
"""

import ui 
import search
import db


def main():
    while True:
        choice = ui.show_menu()
        if choice == 'quit':
            break

        elif choice == 'search':
            search_city()

        elif choice == 'show':
            show()

        
def search_city():
    """ get city. make api calls. show data """
    search.search()


def show():
    """ show all saved city data"""
    all_data = db.get_all()
    ui.display(all_data)


