import yaml
import unittest

sys.path.append('config')

with open('config/secrets.yml', 'r') as file:
	CONFIG = yaml.safe_load(file)

# Define constants
AMADEUS_TOKEN = CONFIG['AMADEUS_KEY']
AMADEUS_SECRET = CONFIG['AMADEUS_SECRET']