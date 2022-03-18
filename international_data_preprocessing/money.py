"""The money module includes an object representation of money,
and functions to parse strings into Money."""
from .country import Country
from ._util import check_single_row
import pandas as pd
import re
import os
import os.path

dirpath = os.path.dirname(os.path.realpath(__file__))
_country_to_currency = pd.read_csv(
    os.path.join(dirpath, 'data/country_currency.csv'))
_currencies = pd.read_csv(os.path.join(dirpath, 'data/currencies.csv'))

_country_to_currency_dict = {}
for row in _country_to_currency.itertuples():
    _country_to_currency_dict[row.country] = row.currency


class Money:
    """The Money class contains all functions to parse and retrieve money values in any currency."""

    def __init__(self, amount, currency_abbv, currency_full=None):
        """Initialize Money instance.

        Args:
            amount: the numeric amount of money, regardless of currency.
            currency_abbv: the 3 letter abbreviation of the currency.
            currency_full: optional, the full name of the currency.
        """
        self.amount = amount
        self.currency_abbv = currency_abbv
        self.currency_full = currency_full

    def get(self, attr):
        """Retrieve attribute from an instance of the Money class.

        Args:
            attr: name of attribute to retrieve, one of (amount, abbv, full).

        Returns:
            the value of the requested attribute.

        Raises:
            ValueError: if the input is not one of the 3 attributes.
        """
        if attr == 'amount':
            return self.amount
        elif attr == 'abbv':
            return self.currency_abbv
        elif attr == 'full':
            return self.currency_full
        else:
            raise ValueError(
                "attr must be one of the following: amount, currency_abbv, currency_full")

    @staticmethod
    def parse(input, currency=None):
        """Parses money value strings into Money objects.

        Args:
            input: string containing the money value in <amount currency> or <currency amount> format, or <amount> format if currency is provided separately.
            currency: optional, string containing the currency code or full currency name.

        Returns:
            the Currency object.

        Raises:
            ValueError: if the input is not in the format specified above.
        """
        input = str(input).strip()

        if currency:
            if not re.fullmatch('[0-9]+\\.?[0-9]*', input):
                raise ValueError(
                    "Input must be a numeric value or number in string representation when currency is specified.")
            row = _currencies[(_currencies['abbreviation'] == currency) | (
                _currencies['full_name'] == currency)]
            check_single_row(row,
                             "Currency provided must be a valid 3 letter abbreviation from https://www.ifcmarkets.com/en/about-forex/currencies-and-abbreviations")
            return Money(
                float(input), row.iloc[0]['abbreviation'], row.iloc[0]['full_name'])

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
                raise ValueError(
                    "Input must be of the form <amount currency> or <currency amount> if currency is not provided.")

        row = _currencies[(_currencies['abbreviation'] == currency) |
                          (_currencies['full_name'] == currency)]
        check_single_row(row,
                         "Currency must be a valid 3 letter abbreviation from https://www.ifcmarkets.com/en/about-forex/currencies-and-abbreviations")
        return Money(
            float(amount), row.iloc[0]['abbreviation'], row.iloc[0]['full_name'])


def country_to_primary_currency(
        df, country_col_name, output_col_name=None, in_place=True):
    """Provides currency code given a country in any standard notation.
    For countries with more than one currency, the primary or most commonly used one is selected.

    Args:
        df: the data frame.
        country_col_name: the name of the column with country in alpha2, alpha3, UN, full, or short format.
        output_col_name: new column name if in_place is False.
        in_place: if True, overwrite output to input column; if False, write output to new column.
    """
    new_col = df[country_col_name].map(Country.parse).map(
        lambda x: _country_to_currency_dict[x.get('alpha3')])

    if in_place:
        df[country_col_name] = new_col
    else:
        if not output_col_name:
            raise ValueError(
                "output_col_name must be provided when operation is not in place.")
        df[output_col_name] = new_col


def parse_money(df, input_col_name, output_types=None,
                     output_col_names=None, in_place=True):
    """Parses and separates money values (e.g. EUR 52.50) into its amount and/or currency.

    Args:
        df: the data frame.
        input_col_name: the name of the column with money values.
        output_types: one or more of ['amount', 'abbv', 'full'].
        output_col_names: new column names if in_place is False.
        in_place: if True, overwrite output to input column; if False, write output to new column.
    """
    new_col = df[input_col_name].map(Money.parse)

    if in_place:
        df[input_col_name] = new_col.map(
            lambda x: str(x.get('amount')) + x.get('abbv'))
    else:
        if len(output_types) != len(output_col_names):
            raise ValueError(
                "output_types and output_col_names must be of the same length")
        for i in range(len(output_types)):
            df[output_col_names[i]] = new_col.map(
                lambda x: x.get(output_types[i]))
