from ._util import check_single_row
import pandas as pd
import os, os.path

dirpath = os.path.dirname(os.path.realpath(__file__))
_inflation = pd.read_csv(os.path.join(dirpath, 'data/inflation.csv'))
_population = pd.read_csv(os.path.join(dirpath, 'data/population.csv'))
_forex = pd.read_csv(os.path.join(dirpath, 'data/forex.csv'))

def _adjust_for_inflation_single(amount, country, year_from, year_to):
	row_from = _inflation[_inflation['year'] == year_from]
	check_single_row(row_from, str(year_from) + " is not a supported year for inflation in " + country)
	row_to = _inflation[_inflation['year'] == year_to]
	check_single_row(row_from, str(year_to) + " is not a supported year for inflation in " + country)

	index_from = row_from.iloc[0]['index']
	index_to = row_to.iloc[0]['index']

	return amount * index_to / index_from

def adjust_for_inflation(df, amount_col, country_col, year_from_col, year_to_col, in_place=True, new_col_name=None):
	new_col = df.apply(lambda x : _adjust_for_inflation_single(x[amount_col], x[country_col], x[year_from_col], x[year_to_col]), axis=1)

	if in_place:
		df[amount_col] = new_col
	else:
		if not new_col_name:
			raise ValueError("new_col_name is required when operation is not in-place")
		df[new_col_name] = new_col


def _adjust_per_capita_single(amount, country, year):
	row = _population[(_population['country'] == country) & (_population['year'] == year)]
	check_single_row(row, "Population data for " + country + " in " + str(year) + " is unavailable")
	return amount / row.iloc[0]['population']


def adjust_per_capita(df, amount_col, country_col, year_col, in_place=True, new_col_name=None):
	new_col = df.apply(lambda x : _adjust_per_capita_single(x[amount_col], x[country_col], x[year_col]), axis=1)

	if in_place:
		df[amount_col] = new_col
	else:
		if not new_col_name:
			raise ValueError("new_col_name is required when operation is not in-place")
		df[new_col_name] = new_col


def _convert_currency_single(amount, currency_from, currency_to, year):
	row = _forex[(_forex['from'] == currency_from) & (_forex['to'] == currency_to) & (_forex['year'] == year)]
	check_single_row(row, "Forex data for " + currency_from + " and " + currency_to + " in " + str(year) + " is unavailable")
	return amount * row.iloc[0]['rate']

def convert_currency(df, amount_col, currency_from_col, currency_to_col, year_col, in_place=True, new_col_name=None):
	new_col = df.apply(lambda x : _convert_currency_single(x[amount_col], x[currency_from_col], x[currency_to_col], x[year_col]), axis=1)

	if in_place:
		df[amount_col] = new_col
	else:
		if not new_col_name:
			raise ValueError("new_col_name is required when operation is not in-place")
		df[new_col_name] = new_col