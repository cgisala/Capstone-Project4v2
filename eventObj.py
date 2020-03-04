class Event_OB:

    # initialization
    def __init__(self, event, place, venue, date,):
        self.event = event
        self.place = place
        self.venue = venue
        self.date = date

    # return string
    def __str__(self):
        return f'{self.event} is taking place {self.place} at {self.venue} on {self.date}'