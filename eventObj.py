import city_event, weather, rest


def create_eventful_objects(EVENT_RESPONSE):
    events = EVENT_RESPONSE['event']
    # list to hold eventful objects
    event_list = []
    for event in events:
        # create object
        event_object = Event_OB
        # fill object with data
        event_object.event = event['title']
        event_object.place = event['city_name']
        event_object.venue = event['venue_name']
        event_object.date = event['start_time']
        # add object to list
        event_list.append(event_object)

    return event_list


class Event_OB():

    # initialization
    def __init__(self, event, place, venue, date, ):
        self.event = event
        self.place = place
        self.venue = venue
        self.date = date

    # return string
    def __str__(self):
        return f'{self.event} is taking place {self.place} at {self.venue} on {self.date}'
