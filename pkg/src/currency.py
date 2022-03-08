from country import Country
import pandas as pd

_country_to_currency = pd.read_csv('data/country_currency.csv')
_currencies = pd.read_csv('data/currencies.csv')

_country_to_currency_dict = {}
for row in _country_to_currency.itertuples():
	_country_to_currency_dict[row.country] = row.currency

class Money:
	def __init__(self, amount, currency_abbv, currency_full=None):
		self.amount = amount
		self.currency_abbv = currency_abbv
		self.currency_full = currency_full

	def get(self, attr):
		if attr == 'amount':
			return self.amount
		elif attr == 'abbv':
			return self.currency_abbv
		elif attr == 'full':
			return self.currency_full
		else:
			raise ValueError("attr must be one of the following: amount, currency_abbv, currency_full")

	@staticmethod
	def parse(input, currency=None):
		input = str(input).strip()

		if currency:
			if not re.fullmatch('[0-9]+\\.?[0-9]*', input):
				raise ValueError("Input must be a number or a number in string representation when currency is specified.")
			row = _currencies[(_currencies['abbreviation'] == currency) | (_currencies['full_name'] == currency)]
			check_single_row(row, '''Currency provided must be a valid 3 letter abbreviation from https://www.ifcmarkets.com/en/about-forex/currencies-and-abbreviations''')
			return Currency(float(input), row.iloc[0]['abbreviation'], row.iloc[0]['full_name'])

		amount = None
		match = re.fullmatch('([0-9]+\\.?[0-9]*)\\s*([a-zA-Z\\s]+)', input)
		if match:
			amount = match.group(0)
			currency = match.group(1)
		else:
			match = re.fullmatch('([a-zA-Z\\s]+)\\s*([0-9]+\\.?[0-9]*)', input)
			if match:
				amount = match.group(1)
				currency = match.group(0)
			else:
				raise ValueError("Input must be of the form <amount currency> or <currency amount> if currency is not provided.")
		
		row = _currencies[(_currencies['abbreviation'] == currency) | (_currencies['full_name'] == currency)]
		check_single_row(row, '''Currency must be a valid 3 letter abbreviation from https://www.ifcmarkets.com/en/about-forex/currencies-and-abbreviations''')
		return Currency(float(input), row.iloc[0]['abbreviation'], row.iloc[0]['full_name'])


def country_to_primary_currency(df, country_col_name, output_col_name=None, in_place=True):
	new_col = df[country_col_name].map(Country.parse).map(lambda x : _country_to_currency_dict[x.get('alpha3')])

	if in_place:
		df[country_col_name] = new_col
	else:
		if not output_col_name:
			raise ValueError("output_col_name must be provided when operation is not in place.")
		df[output_col_name] = new_col


def parse_currencies(df, input_col_name, output_types=None, output_col_names=None, in_place=True):
	new_col = df[input_col_name].map(Currency.parse)

	if in_place:
		df[input_col_name] = new_col.map(lambda x : str(x.get('amount')) + x.get('abbv'))
	else:
		if len(output_types) != len(output_col_names):
			raise ValueError("output_types and output_col_names must be of the same length")
		for i in range(len(output_types)):
			df[output_col_names[i]] = new_col.map(lambda x : x.get(output_types[i]))
