"""
import required files
"""
import unittest
from spec_helper import Client
from spec_helper import AMADEUS_KEY, AMADEUS_SECRET, AmadeusApi, CandidateFlight

"""class for amadeus spec"""
class AmadeusApiSpec(unittest.TestCase):
	def test_token_generator(self):
		"""method to check if token is generated"""
		message = "No token returned"
		defult = None
		token = Client(client_id=AMADEUS_KEY, client_secret=AMADEUS_SECRET)

		self.assertIsNotNone(token, message)

	def test_flight_instance(self):
		"""method to make sure  obtained flights are instances of candidate flights"""
		obtained_flights = AmadeusApi(AMADEUS_KEY,AMADEUS_SECRET). \
			flight('TPE', 'MAD', '2023-10-01', '2023-10-05')

		self.assertIsInstance(obtained_flights, CandidateFlight)


if __name__ == '__main__':
	unittest.main()
