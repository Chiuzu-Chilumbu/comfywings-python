"""
import required files
"""
import pytest
import requests_mock
from spec_helper import AMADEUS_KEY, AMADEUS_SECRET, Request


def test_mock_amadeus_wuth_token():
	client_id = AMADEUS_KEY
	client_secret = AMADEUS_SECRET

	# Mock API response
	mock_response = {
		"access_token" : "test_access_token"
	}

	with requests_mock.Mocker() as m:
		request = Request(client_id, client_secret)

		m.post(request.version1_url_path('security/oauth2/token'), json=mock_response)
		
		# Testing if your method works as expected
		assert request.request_amadeus_auth_token() == "test_access_token"
