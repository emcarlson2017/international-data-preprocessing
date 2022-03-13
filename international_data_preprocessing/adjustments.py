from ._util import check_single_row
import pandas as pd
import os, os.path

dirpath = os.path.dirname(os.path.realpath(__file__))
_inflation = pd.read_csv(os.path.join(dirpath, 'data/inflation.csv'))
_population = pd.read_csv(os.path.join(dirpath, 'data/population.csv'))
_forex = pd.read_csv(os.path.join(dirpath, 'data/forex.csv'))

def _adjust_for_inflation_single(amount, country, year_from, year_to):
    """Adjust a single numeric value for inflation.

    Keyword arguments:
    amount -- numeric value for inflation calculation
    country -- country associated with numeric currency value (alpha 3 code)
    year_from -- year of current currency value 
    year_to -- year of currency value after adjustment
    """
	row_from = _inflation[(_inflation['country'] == country) & (_inflation['year'] == year_from)]
	check_single_row(row_from, str(year_from) + " is not a supported year for inflation in " + country)
	row_to = _inflation[(_inflation['country'] == country) & (_inflation['year'] == year_to)]
	check_single_row(row_from, str(year_to) + " is not a supported year for inflation in " + country)

	index_from = row_from.iloc[0]['index']
	index_to = row_to.iloc[0]['index']

	return amount * index_to / index_from

def adjust_for_inflation(df, amount_col, country_col, year_from_col, year_to_col, in_place=True, new_col_name=None):
    """Adjust a column of numeric values for inflation.

    Keyword arguments:
    df -- data frame 
    amount_col -- numeric value column
    country_col -- country column associated with currency values (alpha 3 code)
    year_from_col -- year column of original currency values 
    year_to_col -- year column of resulting currency values 
    in_place -- if True, overwrite previous column. if False, add a new column of resulting values
    new_col_name -- new column name of resulting values in in_place is False
    """
	new_col = df.apply(lambda x : _adjust_for_inflation_single(x[amount_col], x[country_col], x[year_from_col], x[year_to_col]), axis=1)

	if in_place:
		df[amount_col] = new_col
	else:
		if not new_col_name:
			raise ValueError("new_col_name is required when operation is not in-place")
		df[new_col_name] = new_col


def _adjust_per_capita_single(amount, country, year):
    """Calculate per capita adjustment of a single numeric metric. 

    Keyword arguments:
    amount -- numeric value for per capita adjustment
    country -- country associated with numeric value 
    year -- year associated with numeric value 
    """
	row = _population[(_population['country'] == country) & (_population['year'] == year)]
	check_single_row(row, "Population data for " + country + " in " + str(year) + " is unavailable")
	return amount / row.iloc[0]['population']


def adjust_per_capita(df, amount_col, country_col, year_col, in_place=True, new_col_name=None):
    """Conduct a per capita adjustment on a column of numeric values.

    Keyword arguments:
    df -- data frame
    amount_col -- numeric value column for per capita adjustment 
    country_col -- country column associated with numeric value column (alpha 3 code)
    year_col -- year column associated with numeric value column 
    in_place -- if True, overwrite previous column. if False, add a new column of resulting values
    new_col_name -- new column name of resulting values in in_place is False
    """
	new_col = df.apply(lambda x : _adjust_per_capita_single(x[amount_col], x[country_col], x[year_col]), axis=1)

	if in_place:
		df[amount_col] = new_col
	else:
		if not new_col_name:
			raise ValueError("new_col_name is required when operation is not in-place")
		df[new_col_name] = new_col


def _convert_currency_single(amount, currency_from, currency_to, year):
    """Exchange a currency value. 

    Keyword arguments:
    amount -- currency value
    country_from -- original currency associated with amount value (standard 3 letter currency code)
    country_to -- resulting currency of exchanged value (standard 3 letter currency code)
    year -- year associated with amount value
    """
	if currency_from == currency_to:
		return amount
	row = _forex[(_forex['from'] == currency_from) & (_forex['to'] == currency_to) & (_forex['year'] == year)]
	check_single_row(row, "Forex data for " + currency_from + " and " + currency_to + " in " + str(year) + " is unavailable")
	return amount * row.iloc[0]['rate']

def convert_currency(df, amount_col, currency_from_col, currency_to_col, year_col, in_place=True, new_col_name=None):
     """Exchange a column of currency values. 

    Keyword arguments:
    df -- data frame
    amount_col -- column of currency values
    country_from_col -- original currency column associated with amount column (standard 3 letter currency code)
    country_to_col -- resulting currency column of exchanged column (standard 3 letter currency code)
    year_col -- year column of measured amount column 
    in_place -- if True, overwrite previous column. if False, add a new column of resulting values
    new_col_name -- new column name of resulting values in in_place is False
    """
	new_col = df.apply(lambda x : _convert_currency_single(x[amount_col], x[currency_from_col], x[currency_to_col], x[year_col]), axis=1)

	if in_place:
		df[amount_col] = new_col
	else:
		if not new_col_name:
			raise ValueError("new_col_name is required when operation is not in-place")
		df[new_col_name] = new_col