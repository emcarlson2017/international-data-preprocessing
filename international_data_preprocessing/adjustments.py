"""The adjustments module includes functions to preprocess data involving countries and currencies."""
from ._util import check_single_row
import pandas as pd
import os
import os.path

dirpath = os.path.dirname(os.path.realpath(__file__))
_inflation = pd.read_csv(os.path.join(dirpath, 'data/inflation.csv'))
_population = pd.read_csv(os.path.join(dirpath, 'data/population.csv'))
_forex = pd.read_csv(os.path.join(dirpath, 'data/forex.csv'))


def _adjust_for_inflation_single(amount, country, year_from, year_to):
    row_from = _inflation[(_inflation['country'] == country)
                          & (_inflation['year'] == year_from)]
    check_single_row(row_from, str(year_from) +
                     " is not a supported year for inflation in " + country)
    row_to = _inflation[(_inflation['country'] == country)
                        & (_inflation['year'] == year_to)]
    check_single_row(row_from, str(year_to) +
                     " is not a supported year for inflation in " + country)

    index_from = row_from.iloc[0]['index']
    index_to = row_to.iloc[0]['index']

    return amount * index_to / index_from


def adjust_for_inflation(df, amount_col, country_col, year_from_col,
                         year_to_col, in_place=True, new_col_name=None):
    """Adjust monetary values for inflation.

    Args:
        df: the data frame.
        amount_col: the name of the column containing the numeric amount of money, regardless of currency; see Money.parse.
        country_col: the name of the column containing the name of the country in alpha3 code; see Country.parse.
        year_from_col: the name of the column containing the year the input money values belong to.
        year_to_col: the name of the column containing the year the resulting money values should belong to.
        in_place: if True, overwrite input column; if False, add a new column of resulting values.
        new_col_name: optional, the name of the new column of resulting values if in_place is False.

    Raises:
        ValueError: if new column name is not provided when in_place=False, or the provided years/country combination does not have inflation data.
    """
    new_col = df.apply(lambda x: _adjust_for_inflation_single(
        x[amount_col], x[country_col], x[year_from_col], x[year_to_col]), axis=1)

    if in_place:
        df[amount_col] = new_col
    else:
        if not new_col_name:
            raise ValueError(
                "new_col_name is required when operation is not in-place")
        df[new_col_name] = new_col


def _adjust_per_capita_single(amount, country, year):
    row = _population[(_population['country'] == country)
                      & (_population['year'] == year)]
    check_single_row(row, "Population data for " + country +
                     " in " + str(year) + " is unavailable")
    return amount / row.iloc[0]['population']


def adjust_per_capita(df, amount_col, country_col,
                      year_col, in_place=True, new_col_name=None):
    """Adjust any metric to per-capita, given a country.

    Args:
        df: the data frame.
        amount_col: the name of the column containing the numeric amount to be adjusted.
        country_col: the name of the column containing the name of the country in alpha3 code; see Country.parse.
        year_col: the name of the column containing the year the metric is from; this will be used to determine population.
        in_place: if True, overwrite input column; if False, add a new column of resulting values.
        new_col_name: optional, the name of the new column of resulting values if in_place is False.

    Raises:
        ValueError: if new column name is not provided when in_place=False, or the provided year/country combination does not have population data.
    """
    new_col = df.apply(lambda x: _adjust_per_capita_single(
        x[amount_col], x[country_col], x[year_col]), axis=1)

    if in_place:
        df[amount_col] = new_col
    else:
        if not new_col_name:
            raise ValueError(
                "new_col_name is required when operation is not in-place")
        df[new_col_name] = new_col


def _convert_currency_single(amount, currency_from, currency_to, year):
    if currency_from == currency_to:
        return amount
    row = _forex[(_forex['from'] == currency_from) &
                 (_forex['to'] == currency_to) & (_forex['year'] == year)]
    check_single_row(row, "Forex data for " + currency_from +
                     " and " + currency_to + " in " + str(year) + " is unavailable")
    return amount * row.iloc[0]['rate']


def convert_currency(df, amount_col, currency_from_col,
                     currency_to_col, year_col, in_place=True, new_col_name=None):
    """Convert monetary values from one currency to another.
    The exchange rate used is the average exchange between the two countries for a given year.

    Args:
        df: the data frame.
        amount_col: the name of the column containing the numeric amount of money, regardless of currency; see Money.parse.
        currency_from_col: the name of the column containing the 3 letter currency code of the given monetary value; see Money.parse.
        currency_to_col: the name of the column containing the 3 letter currency code the resulting money values should be in; see Money.parse.
        year_col: the name of the column containing the year to use for the exchange rate.
        in_place: if True, overwrite input column; if False, add a new column of resulting values.
        new_col_name: optional, the name of the new column of resulting values in in_place is False.

    Raises:
        ValueError: if new column name is not provided when in_place=False, or the provided year/currencies combination does not have forex data.
    """
    new_col = df.apply(lambda x: _convert_currency_single(
        x[amount_col], x[currency_from_col], x[currency_to_col], x[year_col]), axis=1)

    if in_place:
        df[amount_col] = new_col
    else:
        if not new_col_name:
            raise ValueError(
                "new_col_name is required when operation is not in-place")
        df[new_col_name] = new_col
