import ui 
import search
import db

def main():

    # Loops until the user choose quit
    while True:
        choice = ui.show_menu() # Calls the show menu function from the ui module and returns the user choice from the menu.
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
    all_data = db.get_all() # Gets all the bookmarked data from the database
    ui.display(all_data)  # Displays all the records from the database.


