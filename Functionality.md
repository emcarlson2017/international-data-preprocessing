# Functionality

An overview of all functionality included in the International Data Preprocessing Python package. 

## Standard Input 

Review the documentation below to ensure the input data frame matches the requirements for each function. 

# Package Functions

## Inflation Adjustments: XXXXX

### Description

This function adjusts currency values for inflation so values are reflective of monetary value for a given year. 

### Arguments

* col_name: Name of the column the inflation adjustment will be excuted on
* year_adjusted: The year to which currency values will be adjusted to 
* in_place: Boolean value to determine if calculation will replace existing column (TRUE) or create a new column (FALSE)
* new_col_name: Name of new column if in_place = TRUE 

### Implementation 

```
code blocks for commands
```

## Per Capita Calculations: XXXX

### Description

This function adjusts numeric values to per-capita values based on an associated country name.  

### Arguments

* col_name: Name of the column the per capita calculation will be executed on 
* country_col_name: Name of column providing country names in data frame 
* in_place: Boolean value to determine if calculation will replace existing column (TRUE) or create a new column (FALSE)
* new_col_name: Name of new column if in_place = TRUE 

### Implementation 

```
code blocks for commands
```

## International Currency Exchange: XXXX 

### Description

This function calculates the exchange value of currency for a given country of origin and given country for calculation. 

### Arguments

* col_name: Name of the column the per capita calculation will be executed on 
* countries: Single value or list of values that determine the exchange calculation 
* in_place: Boolean value to determine if calculation will replace existing column (TRUE) or create a new column (FALSE)
* new_col_name: Name of new column if in_place = TRUE 

### Implementation 

```
code blocks for commands
```

