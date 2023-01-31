from amadeus import Client, ResponseError
import requests
import sys
import yaml
import json


AMADEUS_TOKEN = config['AMADEUS_KEY']
AMADEUS_SECRET = config['AMADEUS_SECRET']

sys.path.append('config')

with open('config/secrets.yml', 'r') as file:
	config = yaml.safe_load(file)

AMADEUS_ROOT = 'https://test.api.amadeus.com'

class Request:
	def __init__(self, token, secret):
		self.token = token
		self.secret = secret

	def version1_url_path(self, path):
		url = '{}/v1/{}'.format(AMADEUS_ROOT, path)
		return url

	def version2_url_path(self, path):
		url = '{}/v2/{}'.format(AMADEUS_ROOT, path)
		return url

	def request_amadeus_token(self):
		postform = {
			'grant_type': 'client_credentials',
			'client_id': self.token,
			'client_secret': self.secret
		}

		url = (self.version1_url_path('security/oauth2/token'))
		headers = {'accept': 'application/x-www-form-urlencoded'}
		response = requests.post(url, data=postform, headers=headers)
		return response.content['access_token']


# Amadeus api class 
class AmadeusApi:
	# Library for amadeus api
	def __init__(self, token, secret):
		self.token = token
		self.secret = secret


	def flight(self, _from, to, from_date, to_date):
		destinations_to = create_destination(1, _from, to, from_date, '10:00:00')
		destination_from = create_destination(2, to, _from, to_date, '17:00:00')
		search = create_filter(destination_to, destination_from)
		project_req_url = version2_url_path('shopping/flight-offers')
		obtain_candidate(project_req_url, search)

	def create_destination(self, id, _from, to, date, time):
		destination = {
			'id': '',
			'originLocationCode': _from,
			'destinatiionLocationCode': to,
			'departureDateTimeRange': {
				'date': '',
				'time': ''
			}
		}
		return destination

	def create_filter(self, origin_destination_to, origin_destination_from):
		filter = {
			currencyCode: 'USD',
			originDestinations: [origin_destination_to, origin_destination_from],
			travelers: [{'id': '1', 'travelerType': 'Adult'}],
			"sources": ['GDS']
		}

	def call_post_url(self, url, content):
		responses = Request(AMADEUS_ROOT, self.token, self.secret)
		
		header = {"accept": 'application/vnd.amadeus+json'}
		auth_token = ("Bearer {}".format(responses.request_amadeus_token()))

		post_request = requests.post(url, auth=auth_token, json=content)

		print(post_request)
		


