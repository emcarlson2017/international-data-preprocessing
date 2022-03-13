# Design 

An overview of the design decisions made during the creation of this Internation Data Preprocessing Python Package. 

## Data Input

This package takes in a data frame at the function level. The purpose of reading a data frame in at the function level is minimizing the amount of code users will have to write. Users are able to conduct general cleaning of their data frame, and then execute a single function to achieve a desired result. 

Once a data frame is read in, it is converted to a pandas dataframe. This decision was made as this is a relatively standard data frame type, allowing for input compatability and standardization of process on the back end. The pandas data frame type also allows us the flexibility necessary for creating new column data types. 

In addition to reading in the data frame, it is also necessary for the users to state which columns the function operations will be performed on, and the data type of those columns. As data types provided by the original data frame can easily cause processing errors, users will select unique data types from a created list. This explicit selection allows for total control on the part of the user, so that their desired outcome is achieved. 

## Functions 

The functions included in this package:XXXX, XXXXX, and XXXX, a

## Calculation Source Data 

## Versioning 

