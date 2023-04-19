"""import required modules"""
from amadeus import Client, ResponseError
from candidate_flight import CandidateFlight
import sys
import yaml
import json

"""add config director to path"""
sys.path.append('config')

with open('config/secrets.yml', 'r') as file:
	config = yaml.safe_load(file)

"""config secrets"""
AMADEUS_KEY = config['AMADEUS_KEY']
AMADEUS_SECRET = config['AMADEUS_SECRET']



"""Amadeus api class""" 
class AmadeusApi:
	# Library for amadeus api
	def __init__(self, token, secret):
		"""authentication values"""
		self.key = AMADEUS_KEY
		self.secret = AMADEUS_SECRET

	def amadeus_client(self):
		"""token generator"""
		amadeus = Client(
			client_id=self.key,
			client_secret=self.secret)

		return amadeus

	def flight(self, _from, _to, _depart_date, _arrival_date):
		"""flight information"""
		amadeus = self.amadeus_client()
		
		response = amadeus.shopping.flight_offers_search.get(
			originLocationCode=_from,
			destinationLocationCode=_to,
			departureDate=_depart_date,
			returnDate=_arrival_date,
			currencyCode='USD',
			adults=1)

		return CandidateFlight(response.result)


