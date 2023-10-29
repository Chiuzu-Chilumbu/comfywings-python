import sys
import pytest

sys.path.append('tests/helpers')

from tests_helper import AMADEUS_KEY, AMADEUS_SECRET, Request, Response

@pytest.mark.skip
def test_should_return_amadeus_authorisation_token():
	# Given : the correct client credentials
	AmadeusRequest = Request(AMADEUS_KEY, AMADEUS_SECRET)

	# When : Retriveing the authentication token
	auth_token = AmadeusRequest.request_amadeus_auth_token()

	# Then : Token must not be none and must have a length greater than 0
	assert auth_token is not None
	assert len(auth_token) > 0


def test_should_return_401_unauthorised_error_with_invalid_credentials():
	# Given : the incorrect client credentials
	AmadeusRequest = Request("WRONG_KEY", "WRONG_SECRET")

	# When : retriving the authentication token
	try:
		auth_token = AmadeusRequest.request_amadeus_auth_token()
	except Response.Unauthorized:
		# Then : unauthorised error response should be given
		assert True
	
	except Exception as e:
		pytest.fail(f"Expected Response.unauthorised response but instead got {type(e)}")
	else:
		pytest.fail("Expected Response.unauthorised but no error was raised")
