# International Data Preprocessing

## country.py

The country module includes an object representation of a country, and functions to parse strings into Countries.

### class Country

The Country class contains all related identifying codes and names for a given country.

#### constructor

Initialize country instance.

Args:
* alpha2_code: official two letter identifying country code.
* alpha3_code: official three letter identifying country code.
* un_code: official 3 digit country code assigned by the United Nations.
* full_name: full official name of country.
* short_name: shortened official name of country.

#### get

Retrieve attribute from an instance of the Country class.

Args:
* attr: name of attribute to retrieve, one of (alpha2, alpha3, UN, full, short).

Returns:
* the value of the requested attribute.

Raises:
* ValueError: if the input is not one of the 5 attributes.

#### parse (static method)

Parses country string into a Country object. This method will automatically fill out the other 4 attributes based on any 1 attribute.

Args:
* input: country string of type alpha2, alpha3, UN code, short name, or full name.

Returns:
* the Country object.

Raises:
* ValueError: if the input is not in one of the 5 formats.

### parse_countries

Parses the input from any valid country representation and outputs in the desired format.

Args:
* df: the data frame.
* input_col_name: the name of column with country strings.
* output_types: one or more of ['alpha2', 'alpha3', 'UN', 'full', 'short'], 'alpha2' by default.
* output_col_names: name(s) of new column(s) if in_place is False.
* in_place: if True, overwrite output to same column; if False, write output to new column(s).

Raises:
* ValueError: if the input column cannot be parsed, or if the requested output type is not one of 5 accepted values.

## money.py

The money module includes an object representation of money, and functions to parse strings into Money.

### class Money

The Money class contains all functions to parse and retrieve money values in any currency.

#### constructor

Initialize Money instance.

Args:
* amount: the numeric amount of money, regardless of currency.
* currency_abbv: the 3 letter abbreviation of the currency.
* currency_full: optional, the full name of the currency.

#### get

Retrieve attribute from an instance of the Money class.

Args:
* attr: name of attribute to retrieve, one of (amount, abbv, full).

Returns:
* the value of the requested attribute.

Raises:
* ValueError: if the input is not one of the 3 attributes.

#### parse (static method)

Parses money value strings into Money objects.

Args:
* input: string containing the money value in \<amount currency\> or \<currency amount\> format, or \<amount\> format if currency is provided separately.
* currency: optional, string containing the currency code or full currency name.

Returns:
* the Currency object.

Raises:
* ValueError: if the input is not in the format specified above.

### country_to_primary_currency

Provides currency code given a country in any standard notation. For countries with more than one currency, the primary or most commonly used one is selected.

Args:
* df: the data frame.
* country_col_name: the name of the column with country in alpha2, alpha3, UN, full, or short format.
* output_col_name: new column name if in_place is False.
* in_place: if True, overwrite output to input column; if False, write output to new column.

### parse_money

Parses and separates money values (e.g. EUR 52.50) into its amount and/or currency.

Args:
* df: the data frame.
* input_col_name: the name of the column with money values.
* output_types: one or more of ['amount', 'abbv', 'full'].
* output_col_names: new column names if in_place is False.
* in_place: if True, overwrite output to input column; if False, write output to new column.

## adjustments.py

The adjustments module includes functions to preprocess data involving countries and currencies.

### adjust_for_inflation

Adjust monetary values for inflation.

Args:
* df: the data frame.
* amount_col: the name of the column containing the numeric amount of money, regardless of currency; see Money.parse.
* country_col: the name of the column containing the name of the country in alpha3 code; see Country.parse.
* year_from_col: the name of the column containing the year the input money values belong to.
* year_to_col: the name of the column containing the year the resulting money values should belong to.
* in_place: if True, overwrite input column; if False, add a new column of resulting values.
* new_col_name: optional, the name of the new column of resulting values if in_place is False.

Raises:
* ValueError: if new column name is not provided when in_place=False, or the provided years/country combination does not have inflation data.

### adjust_per_capita

Adjust any metric to per-capita, given a country.

Args:
* df: the data frame.
* amount_col: the name of the column containing the numeric amount to be adjusted.
* country_col: the name of the column containing the name of the country in alpha3 code; see Country.parse.
* year_col: the name of the column containing the year the metric is from; this will be used to determine population.
* in_place: if True, overwrite input column; if False, add a new column of resulting values.
* new_col_name: optional, the name of the new column of resulting values if in_place is False.

Raises:
* ValueError: if new column name is not provided when in_place=False, or the provided year/country combination does not have population data.

### convert_currency

Convert monetary values from one currency to another. The exchange rate used is the average exchange between the two countries for a given year.

Args:
* df: the data frame.
* amount_col: the name of the column containing the numeric amount of money, regardless of currency; see Money.parse.
* currency_from_col: the name of the column containing the 3 letter currency code of the given monetary value; see Money.parse.
* currency_to_col: the name of the column containing the 3 letter currency code the resulting money values should be in; see Money.parse.
* year_col: the name of the column containing the year to use for the exchange rate.
* in_place: if True, overwrite input column; if False, add a new column of resulting values.
* new_col_name: optional, the name of the new column of resulting values in in_place is False.

Raises:
* ValueError: if new column name is not provided when in_place=False, or the provided year/currencies combination does not have forex data.
