import sys
import unittest
import spec_helper
from spec_helper import Client
from spec_helper import AMADEUS_KEY, AMADEUS_SECRET, AmadeusApi, CandidateFlight




class AmadeusApiSpec(unittest.TestCase):
	# check if token has been genereated
	def test_token_generator(self):
		message = "No token returned"
		defult = None
		token = Client(client_id=AMADEUS_KEY, client_secret=AMADEUS_SECRET)

		self.assertIsNotNone(token, message)

	def test_flight_instance(self):
		#amadeus instance
		obtained_flights = AmadeusApi(AMADEUS_KEY,AMADEUS_SECRET).flight('TPE', 'MAD', '2023-10-01', '2023-10-05')

		self.assertIsInstance(obtained_flights, CandidateFlight)


if __name__ == '__main__':
	unittest.main()

