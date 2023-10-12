"""import required modules"""
import sys
import yaml
import json
import requests

from amadeus import Client, ResponseError
from candidate_flight import CandidateFlight

"""add config director to path"""
sys.path.append('config')

with open('config/secrets.yml', 'r') as file:
	config = yaml.safe_load(file)

"""config secrets"""
AMADEUS_KEY = config['AMADEUS_KEY']
AMADEUS_SECRET = config['AMADEUS_SECRET']

import requests

class AmadeusMixin():
    AMADEUS_API_ENDPOINT = 'https://test.api.amadeus.com'

class AmadeusApi(AmadeusMixin):
    def __init__(self, token, secret):
        self.token = token
        self.secret = secret

    def call_post_usr(self, url, post_content):
        # Note: The `Request` class initialization requires two arguments
        responses = Request(self.token, self.secret).request_amadeus_auth_token()

class Request(AmadeusMixin):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def version1_url_path(self, path):
        return "{}/v1/{}".format(self.AMADEUS_API_ENDPOINT, path)

    def version2_url_path(self, path):
        return "{}/v2/{}".format(self.AMADEUS_API_ENDPOINT, path)

    def request_amadeus_auth_token(self):
        payload = 'client_id={}&client_secret={}&grant_type=client_credentials'.format(self.client_id, self.client_secret)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", self.version1_url_path('security/oauth2/token'), headers=headers, data=payload)

        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print(f"Failed to retrieve token: {response.text}")
            return None

class Response():
    class BadRequest(Exception):
        """A class to raise the bad request HTTP error."""
        pass

    class Unauthorized(Exception):
        """A class to raise the unauthorized HTTP error."""
        pass

    class Unexpected(Exception):
        """A class to raise an unexpected error."""
        pass

    HTTP_ERROR = {
        400: BadRequest,
        401: Unauthorized,
        500: Unexpected
    }

    def __init__(self, code):
        self.code = code
    
    def is_successful(self):
        """Return True if response is successful, False otherwise."""
        return self.code not in self.HTTP_ERROR
    
    def error(self):
        """Return the appropriate error class for the response code."""
        return self.HTTP_ERROR.get(self.code)


# Usage examples
response = Response(200)
print(f"Is Successful? {response.is_successful()}")

response = Response(401)
print(f"Is Successful? {response.is_successful()}")
if not response.is_successful():
    error = response.error()
    raise error("Unauthorized access - invalid credentials")


