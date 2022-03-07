import re
import pandas as pd

_countries = pd.read_csv('../data/countries.csv')

class Country:
	"""docstring for Country"""
	def __init__(self, alpha2_code, alpha3_code=None, un_code=None, full_name=None, short_name=None):
		self.alpha2_code = alpha2_code
		self.alpha3_code = alpha3_code
		self.un_code = un_code
		self.full_name = full_name
		self.short_name = short_name

	@staticmethod
	def _check_valid(row, msg):
		if _countries.shape[0] < 1:
			raise ValueError(msg)
		# unlikely to happen unless someone tampered with /data
		if _countries.shape[0] > 1:
			raise RuntimeError('Module data has been corrupted')

	@staticmethod
	def _row_to_country(row):
		# even though we know that we will get a single row,
		# pandas returns a dataframe when indexing by condition
		row = row.iloc[0]
		return Country(row['alpha2_code'], row['alpha3_code'], row['un_code'], row['full_name'], row['short_name'])

	@staticmethod
	def parse(input):
		input = input.strip()

		if re.fullmatch('[a-zA-Z]{2}', input):
			row = _countries[_countries['alpha2_code'] == input]
			Country._check_valid(row, "Two letter input must be a valid Alpha 2 country code.")
			return Country._row_to_country(row)
		elif re.fullmatch('[a-zA-Z]{3}', input):
			row = _countries[_countries['alpha3_code'] == input]
			Country._check_valid(row, "Three letter input must be a valid Alpha 3 country code.")
			return Country._row_to_country(row)
		elif re.fullmatch('\\d{2}', input):
			row = _countries[_countries['alpha2_code'] == input]
			Country._check_valid(row, "Three digit input must be a valid UN country code.")
			return Country._row_to_country(row)
		else:
			row = _countries[_countries['full_name'] == input | _countries['short_name'] == input]
			Country._check_valid(row, '''Please provide 2 letter Alpha 2 code, or 3 letter Alpha 3 code, or 3 digit UN code or the official or shortened name of a country from https://www.un.int/protocol/sites/www.un.int/files/Protocol%20and%20Liaison%20Service/officialnamesofcountries.pdf''')
			return Country._row_to_country(row)


		