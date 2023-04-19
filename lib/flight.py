"""class for individual flights"""

class Flight :
    """.flight class"""
    def __init__(self, flight_data):
        self.flight_data = flight_data

    def outbound_duration(self):
        """outboun flight duration"""
        return self.flight_data['itineraries'][0]['duration']

    def inbound_duration(self):
        """inbound flight duration"""
        return self.flight_data['itineraries'][1]['duration']

    def total_price(self):
        """flight total price"""
        return self.flight_data['price']['total']