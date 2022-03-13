# Functionality

An overview of all preprocessing functionality included in the International Data Preprocessing Python package. 

## Standard Input 

Review the documentation below to ensure the input column types match the requirements for each function. 

## Inflation Adjustments: adjust_for_inflation

### Description

This function adjusts numeric monetary values for inflation based on year and country values. 

### Arguments

* df: data frame 
* amount_col: numeric monetary value column to be adjusted
* country_col: country column associated with currency values (must be in alpha 3 code format)
* year_from_col: year column of original currency values 
* year_to_col: year column of resulting currency values 
* in_place: if True, overwrite previous column; if False, add a new column of resulting values

For implementation, see Example 2 in the examples file. 

## Per Capita Calculations: adjust_per_capita

### Description

This function adjusts numeric values to per-capita values based on an associated country and year.  

### Arguments

* df: data frame
* amount_col: numeric value column for per capita adjustment 
* country_col: country column associated with numeric value column (must be in alpha 3 code format)
* year_col: year column associated with numeric value column 
* in_place: if True, overwrite previous column; if False, add a new column of resulting values
* new_col_name: new column name of resulting values if in_place is False

For function implementation, see Example 1 in the examples folder. 

## International Currency Exchange: convert_currency 

### Description

This function calculates the exchange value from one currency to another. 

### Arguments

* df: data frame
* amount_col: column of monetary values
* country_from_col: original currency column associated with amount column (must be in standard 3 letter currency codes)
* country_to_col: resulting currency type column of exchanged amount column (must be in standard 3 letter currency codes)
* year_col: year column of measured amount 
* in_place: if True, overwrite previous column; if False, add a new column of resulting values
* new_col_name: new column name of resulting values if in_place is False

For function implementation, see Example 3 in the examples folder. 
