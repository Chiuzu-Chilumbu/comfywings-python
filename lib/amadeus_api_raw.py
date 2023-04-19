"""import required modules"""
import sys
from amadeus import Client
import yaml


sys.path.append('config')
sys.path.append('spec/fixtures')

with open('config/secrets.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)

amadeus = Client(
    client_id=CONFIG['AMADEUS_KEY'],
    client_secret=CONFIG['AMADEUS_SECRET']
)


response = amadeus.shopping.flight_offers_search.get(
    originLocationCode='TPE',
    destinationLocationCode='MAD',
    departureDate='2023-10-01',
	returnDate='2023-10-05',
	currencyCode='USD',
    adults=1)

# write to yaml files
with open('spec/fixtures/flight_results.yml', 'w') as file:
    flight_results = yaml.dump(response.result, file)
