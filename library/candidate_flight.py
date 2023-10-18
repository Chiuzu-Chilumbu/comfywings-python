"""import required modules and files"""
from flight import Flight


class CandidateFlight :
    """candidate flight class"""
    def __init__(self, flight_info):
        self.flight_info = flight_info

    def individual_flights(self):
        """individual float"""
        array_of_flights = []
        for flights in self.flight_info['data']:
            new_flight = Flight(flights)
            array_of_flights.append(new_flight)
        return array_of_flights
