import sys
import yaml
import flight


class CandidateFlight :
	# class for flights
	def __init__(self, flight_info):
		self.flight_info = flight_info

	def individual_flights(self):
		array_of_flights = []
		for flights in self.flight_info['data']:
			new_flight = Flight(flights)
			array_of_flights.append(new_flight)
		
		return array_of_flights