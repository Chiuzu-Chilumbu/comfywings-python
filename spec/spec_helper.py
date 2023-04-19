"""import needed moduels"""
import sys
import unittest
import yaml
from amadeus import Client, ResponseError


sys.path.append('config')
sys.path.append('spec/fixtures')
sys.path.append('lib')

"""import classes from files in path"""
from candidate_flight import CandidateFlight
from amadeus_api_class import AmadeusApi

with open('config/secrets.yml', 'r') as file:
	CONFIG = yaml.safe_load(file)

with open('spec/fixtures/flight_results.yml', 'r') as file:
	YAML_CORRECT = yaml.safe_load(file)

# Define constants
AMADEUS_KEY = CONFIG['AMADEUS_KEY']
AMADEUS_SECRET = CONFIG['AMADEUS_SECRET']

# needed for unit testing
CORRECT = YAML_CORRECT['data']
