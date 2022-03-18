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