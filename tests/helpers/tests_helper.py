"""import needed moduels"""
import sys
import yaml

sys.path.append('library')

"""import classes from files in path"""
from amadeus_api import Request, Response

with open('config/secrets.yml', 'r') as file:
	CONFIG = yaml.safe_load(file)

with open('tests/fixtures/flight_results.yml', 'r') as file:
	YAML_CORRECT = yaml.safe_load(file)

# Define constants
AMADEUS_KEY = CONFIG['AMADEUS_KEY']
AMADEUS_SECRET = CONFIG['AMADEUS_SECRET']
CORRECT = YAML_CORRECT['data']
