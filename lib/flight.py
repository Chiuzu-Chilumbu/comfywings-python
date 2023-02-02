# Class to store flight information

class Flight :
	def __init__(self, flight_data):
		self.flight_data = flight_data
	
	def outbound_duration(self):
		self.flight_data['itineraries'][0]['duration']

	def inbound_duration(self):
		self.flight_data['itineraries'][1]['duration']

	def total_price(self):
		self.flight_data['price']['total']