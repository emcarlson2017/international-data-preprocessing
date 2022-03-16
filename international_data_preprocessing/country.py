from ._util import check_single_row
import re
import os
import os.path
import pandas as pd

dirpath = os.path.dirname(os.path.realpath(__file__))
_countries = pd.read_csv(os.path.join(dirpath, 'data/countries.csv'))


class Country:
    """The Country class contains all related identifying codes and names for a given country."""

    def __init__(self, alpha2_code, alpha3_code=None,
                 un_code=None, full_name=None, short_name=None):
        """Initialize country instance.

	    Args:
    	    alpha2_code: official two letter identifying country code.
    	    alpha3_code: official three letter identifying country code.
    	    un_code: official 3 digit country code assigned by the United Nations.
    	    full_name: full official name of country.
    	    short_name: shortened official name of country.
        """
       self.alpha2_code = alpha2_code
       self.alpha3_code = alpha3_code
       self.un_code = un_code
       self.full_name = full_name
       self.short_name = short_name

    def get(self, attr):
        """Retrieve attribute from an instance of the Country class.

        Args:
            attr: name of attribute to retrieve, one of (alpha2, alpha3, UN, full, short).

        Returns:
            the value of the requested attribute.

        Raises:
            ValueError: if the input is not one of the 5 attributes.
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
            raise ValueError(
                "attr must be one of the following: alpha2, alpha3, UN, full, short")

    @staticmethod
    def _row_to_country(row):
        # even though we know that we will get a single row,
        # pandas returns a dataframe when indexing by condition
        row = row.iloc[0]
        return Country(row['alpha2_code'], row['alpha3_code'],
                       row['un_code'], row['full_name'], row['short_name'])

    @staticmethod
    def parse(input):
        """Parses country string into a Country object.
        This method will automatically fill out the other 4 attributes based on any 1 attribute.

        Args:
            input: country string of type alpha2, alpha3, UN code, short name, or full name.

        Returns:
            the Country object.

        Raises:
            ValueError: if the input is not in one of the 5 formats.
        """
        input = input.strip()

        if re.fullmatch('[a-zA-Z]{2}', input):
            row = _countries[_countries['alpha2_code'] == input]
            check_single_row(
                row, "Two letter input must be a valid Alpha 2 country code.")
            return Country._row_to_country(row)
        elif re.fullmatch('[a-zA-Z]{3}', input):
            row = _countries[_countries['alpha3_code'] == input]
            check_single_row(
                row, "Three letter input must be a valid Alpha 3 country code.")
            return Country._row_to_country(row)
        elif re.fullmatch('\\d{2}', input):
            row = _countries[_countries['alpha2_code'] == input]
            check_single_row(
                row, "Three digit input must be a valid UN country code.")
            return Country._row_to_country(row)
        else:
            row = _countries[(_countries['full_name'] == input)
                             | (_countries['short_name'] == input)]
            check_single_row(row, "Please provide 2 letter Alpha 2 code, or 3 letter Alpha 3 code, or 3 digit UN code or the official or shortened name of a country from https://www.un.int/protocol/sites/www.un.int/files/Protocol%20and%20Liaison%20Service/officialnamesofcountries.pdf")
            return Country._row_to_country(row)


def parse_countries(df, input_col_name, output_types=[
                    'alpha2'], output_col_names=None, in_place=True):
    """Parses the input from any valid country representation and outputs in the desired format.

    Args:
        df: the data frame.
        input_col_name: the name of column with country strings.
        output_types: one or more of ['alpha2', 'alpha3', 'UN', 'full', 'short'], 'alpha2' by default.
        output_col_names: name(s) of new column(s) if in_place is False.
        in_place: if True, overwrite output to same column; if False, write output to new column(s).

    Raises:
        ValueError: if the input column cannot be parsed, or if the requested output type is not one of 5 accepted values.
    """
    if len(output_types) == 0:
        raise ValueError(
            "output_types must contain one or more of the following: alpha2, alpha3, UN, full, short")

    new_col = df[input_col_name].map(Country.parse)

    if in_place:
        if len(output_types) > 1:
            raise ValueError(
                "Cannot create multiple columns in place, len(output_types) must be 1.")
        df[input_col_name] = new_col.map(lambda x: x.get(output_types[0]))
    else:
        if len(output_types) != len(output_col_names):
            raise ValueError(
                "output_types and output_col_names must be of the same length")
        for i in range(len(output_types)):
            df[output_col_names[i]] = new_col.map(
                lambda x: x.get(output_types[i]))
