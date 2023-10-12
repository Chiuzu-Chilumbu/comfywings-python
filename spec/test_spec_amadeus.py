"""
import required files
"""
import pytest
from spec_helper import AMADEUS_KEY, AMADEUS_SECRET, Request

"""method to check for amadeus token"""

def test_amadeus_auth_token():
	client_id = AMADEUS_KEY
	client_secret=AMADEUS_SECRET

	# Request object instance
	request = Request(client_id, client_secret)
	auth_token = request.request_amadeus_auth_token()
	assert isinstance(auth_token, str) and len(auth_token) > 0
		
"""	
def test_mock_amadeus_wuth_token():
	client_id = AMADEUS_KEY
	client_secret = AMADEUS_SECRET

	# Mock API response
	mock_response = {
		"access_token" : "test_access_token"
	}

	with requests_mock.Mocker() as m:
		request = Request(client_id, client_secret)

		m.post(request_obj.version1_url_path('security/oauth2/token'), json=mock_response)
		
		# Testing if your method works as expected
		assert request_obj.request_amadeus_auth_token() == "test_access_token"
"""
"""
class AmadeusApiSpec(unittest.TestCase):
	def test_token_generator(self):
		message = "No token returned"
		defult = None
		token = Client(client_id=AMADEUS_KEY, client_secret=AMADEUS_SECRET)

		self.assertIsNotNone(token, message)

	def test_flight_instance(self):
		obtained_flights = AmadeusApi(AMADEUS_KEY,AMADEUS_SECRET). \
			flight('TPE', 'MAD', '2023-10-01', '2023-10-05')

		self.assertIsInstance(obtained_flights, CandidateFlight)


if __name__ == '__main__':
	unittest.main()
"""