# Design 

An overview of the design decisions made during the creation of this Python package. 

## Data Input

This package takes in a data frame at the function level. The purpose of reading a data frame in at the function level is minimizing the amount of code users will have to write. Users are able to conduct general cleaning of their data frame, and then execute a single function to achieve a desired result. 

Once a data frame is read in, it is converted to a pandas dataframe. This decision was made as this is a relatively standard data frame type, allowing for input compatability and standardization of process on the back end. The pandas data frame type also allows us the flexibility necessary for creating new column data types. 

In addition to reading in the data frame, it is also necessary for the users to state which columns the function operations will be performed on, and the data type of those columns. As data types provided by the original data frame can easily cause processing errors, users will select unique data types from a created list. This explicit selection allows for total control on the part of the user, so that their desired outcome is achieved. 

## Functions 

The functions included in this package:XXXX, XXXXX, and XXXX, all follow the same design structure. Each function takes in a dataframe that has been structured according to standardized input guidelines and given appropriate column data types. Along with this data frame, the function takes in other arguments that allow the function logic to determine what necessary calculations need to be executed and what necessary data needs to be pulled from the uplodaded CSV file.

The process of executing each of these functions is the same, which is necessary for lessening the learning curve of using this package. Once this data frame is in the appropriate format, users are able to input the data frame into any of the package functions along with additional arguments that will produce the appropriate end-result as determined by the user. This standardized format and process allows these modules to be deeper.  

## Calculation Source Data 

In order to make calculations such as per capita metrics, currency exchanges, and inflation adjustments, it is necessary to pull in additional data not given by the user. Data requirements include country populations, inflation rates by year, and international currency exchange rates. While there are many ways to pull in these values, the design decision made for this project was to create one master data file. 

Maintaining one data file with all associated international data calculation values increases computing efficiency as this file only needs to be uploaded once. Additionally, this file promotes extensibility, so that new values or metrics could be easily added for version updates or scheduled data adjustments. This allows updates to be made to the program without alterations to the program itself, rather, just to its sourced data file. 

## Versioning 

The design structure of this package acknowledges the needs of updates to be made easily and efficiently. Due to the nature of the metrics calculated, it is important to make calculations with the most up-to-date metrics possible. For this reason, this package emphasizes the potential for versioning in its design. As stated previously, the main data source for executing calculations is a maintained data file that is easily updated to provide relevant and accurate calculation metrics. 

Beyond this, the potential for this package to provide more functions in relation to international data pre-processing is evident. Conversions such as time-zone adjustments and percentage of global populations are just a few potential functions that could be added to this package in future versions. 
