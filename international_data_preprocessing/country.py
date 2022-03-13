from ._util import check_single_row
import re
import os, os.path
import pandas as pd

dirpath = os.path.dirname(os.path.realpath(__file__))
_countries = pd.read_csv(os.path.join(dirpath, 'data/countries.csv'))


class Country:
	"""The Country class contains all related identifying codes and names for a given country. 
    This class also contains functions needed to retrieve these names and codes and
    parse these identifiers for a single instance or column. 
    
    Parameters: 
    alpha2_code -- official two letter identifying country code 
    alpha3_code -- official three letter identifying country code
    un_code -- official 3 digit country code assigned by the United Nations 
    full_name -- full official name of country 
    short_name -- shortened official name of country 
    """
	def __init__(self, alpha2_code, alpha3_code=None, un_code=None, full_name=None, short_name=None):
    """Initialize country class"""
		self.alpha2_code = alpha2_code
		self.alpha3_code = alpha3_code
		self.un_code = un_code
		self.full_name = full_name
		self.short_name = short_name

	def get(self, attr):
    """Get an attribute of country class 

    Keyword arguments:
    self -- instance of country class
    attr -- specify country identifier type to retrieve 
    """    
		if attr == 'alpha2':
			return self.alpha2_code
		elif attr == 'alpha3':
			return self.alpha3_code
		elif attr == 'UN':
			return self.un_code
		elif attr == 'full':
			return self.full_name
		elif attr == 'short':
			return self.short_name
		else:
			raise ValueError("attr must be one of the following: alpha2, alpha3, UN, full, short")

	@staticmethod
	def _row_to_country(row):
		# even though we know that we will get a single row,
		# pandas returns a dataframe when indexing by condition
		row = row.iloc[0]
		return Country(row['alpha2_code'], row['alpha3_code'], row['un_code'], row['full_name'], row['short_name'])

	@staticmethod
	def parse(input):
    """Parse standard country input into expected alpha 3 codes for function input

    Keyword arguments:
    input -- country identifier of type alpha 2, alpha 3, shortened name, or full name
    """
		input = input.strip()

		if re.fullmatch('[a-zA-Z]{2}', input):
			row = _countries[_countries['alpha2_code'] == input]
			check_single_row(row, "Two letter input must be a valid Alpha 2 country code.")
			return Country._row_to_country(row)
		elif re.fullmatch('[a-zA-Z]{3}', input):
			row = _countries[_countries['alpha3_code'] == input]
			check_single_row(row, "Three letter input must be a valid Alpha 3 country code.")
			return Country._row_to_country(row)
		elif re.fullmatch('\\d{2}', input):
			row = _countries[_countries['alpha2_code'] == input]
			check_single_row(row, "Three digit input must be a valid UN country code.")
			return Country._row_to_country(row)
		else:
			row = _countries[(_countries['full_name'] == input) | (_countries['short_name'] == input)]
			check_single_row(row, '''Please provide 2 letter Alpha 2 code, or 3 letter Alpha 3 code, or 3 digit UN code or the official or shortened name of a country from https://www.un.int/protocol/sites/www.un.int/files/Protocol%20and%20Liaison%20Service/officialnamesofcountries.pdf''')
			return Country._row_to_country(row)


def parse_countries(df, input_col_name, output_types=['alpha2'], output_col_names=None, in_place=True):
    """Parse country column input to specified identifer type 

    Keyword arguments:
    df -- data frame
    input_col_name -- name of column containing original country identifiers of type alpha 2, alpha 3, shortened name, or full name
    output_types -- country identifer type(s) of desired output 
    output_col_names -- name of new column(s) if in_place is True 
    in_place -- if True, overwrite output to same column(s). If False, write output to new column(s) 
    """
	if len(output_types) == 0:
		raise ValueError("output_types must contain one or more of the following: alpha2, alpha3, UN, full, short")
	
	new_col = df[input_col_name].map(Country.parse)

	if in_place:
		if len(output_types) > 1:
			raise ValueError("Cannot create multiple columns in place, len(output_types) must be 1.")
		df[input_col_name] = new_col.map(lambda x : x.get(output_types[0]))
	else:
		if len(output_types) != len(output_col_names):
			raise ValueError("output_types and output_col_names must be of the same length")
		for i in range(len(output_types)):
			df[output_col_names[i]] = new_col.map(lambda x : x.get(output_types[i]))
