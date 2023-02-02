import yaml
import unittest

sys.path.append('lib/*')
sys.path.append('config')
sys.path.append('spec/fixtures')


with open('config/secrets.yml', 'r') as file:
	CONFIG = yaml.safe_load(file)

with open('spec/fixtures/flight_results.yml', 'r') as file:
	CORRECT = yaml.safe_load(file)

# Define constants
AMADEUS_TOKEN = CONFIG['AMADEUS_KEY']
AMADEUS_SECRET = CONFIG['AMADEUS_SECRET']
