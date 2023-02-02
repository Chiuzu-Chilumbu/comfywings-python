from amadeus import Client, ResponseError
import candidate_flight.py
import sys
import yaml
import json


AMADEUS_TOKEN = config['AMADEUS_KEY']
AMADEUS_SECRET = config['AMADEUS_SECRET']

sys.path.append('config')

with open('config/secrets.yml', 'r') as file:
	config = yaml.safe_load(file)


# Amadeus api class 
class AmadeusApi:
	# Library for amadeus api
	def __init__(self, token, secret):
		self.token = token
		self.secret = secret

	def amadeus_client(self):
		amadeus = Client(
			client_id=CONFIG['AMADEUS_KEY'],
			client_secret=CONFIG['AMADEUS_SECRET'])

		return amadeus

	def flight(self, amadues_, _from, _to, _depart_date, _arrival_date):
		response = amadeus_.shopping.flight_offers_search.get(
			originLocationCode=_from,
			destinationLocationCode=_to,
			departureDate=_depart_date,
			returnDate=_arrival_date,
			currencyCode='USD',
			adults=1)

		CandidateFlight.new(response.result)



class Response():

	HTTP_ERROR = {
		400: 'BadRequest',
		401: 'Unauthorized',
		500: 'Unexpected'
	}

	def __init__():
		pass

	def successful():
		pass

	def error():
		pass 