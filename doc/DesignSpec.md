# Design 

An overview of the design decisions made during the creation of this Internation Data Preprocessing Python Package. 

## Data Input

This package takes in a data frame at the function level. The purpose of reading a data frame in at the function level is minimizing the amount of code users will have to write. Users are able to conduct general cleaning of their data frame, parse the columns associated with their desired calculation to match expected input, and then execute a single function to achieve a desired result. 

Inputted data frames are expected to be pandas data frames. This decision was made as this is a relatively standard data frame type, allowing for input compatability and standardization of process on the back end. 

In addition to reading in the data frame, it is also necessary for the users to state which columns the function operations will be performed on. Some columns will the values adjustments or calculations will be performed on (e.g. numeric monetary value columns). In other cases, the columns passed in will provide additional information necessary to execute desired calculations (e.g. year, country, or currency columns). Columns providing information such as currency type or country identifiers should be of expected standardized input. This standardized input can take the form of alpha 2 codes, alpha 3 codes, UN numeric codes, shortened name, and full name. This allows users to understand exactly what input is expected, and reduces potential errors during function executions. Parsing functions are available to users in order to prepare their data frames with the expected input values for each preprocessing function (i.e. parsing country name to primary currency).  

## Functions 

There are three preprocessing functions included in this package: adjust_for_inflation, adjust_per_capita, and convert_currency. These three functions follow a similar design structure. Each function takes in a dataframe that has been parsed according to expected input guidelines. Along with this data frame, the function takes in other arguments that allow the function logic to determine what calculations need to be executed and what data needs to be pulled from the main CSV file containing population values, inflation rates, etc. Therefore, once the function insures all input values are of the expected format, the values or columns provided identify calculation values to be drawn from the CSV file, the adjustment calculation is executed, and finally the resulting value or column is returned to the user. 

In terms of expected input for each function, precise documentation is provided for each function. Generally speaking, each argument inputted into each function has an expected input type. For example, the per capita adjustment function requires a country value or column as input. This column or value must be provided using the country's standard alpha 3 code. For instances in which the format of the column needs to be changed for function execution to occur, both the country classes and money classes provide extensive parsing functionality to prepare columns or values for function input. 

Overall, the general process for executing each of these functions is very similar, which is necessary for lessening the learning curve for users utilizing this package. This standardized format and process allows these modules to be deeper.  

## Calculation Source Data 

In order to make calculations such as per capita metrics, currency exchanges, and inflation adjustments, it is necessary to pull in additional data not given by the user. Data requirements include country populations, inflation rates by year, and international currency exchange rates. While there are many ways to pull in these values, the design decision made for this project was to create one master data file. 

Maintaining one data file with all associated international data calculation values increases computing efficiency as this file only needs to be uploaded once. Additionally, this file promotes extensibility, so that new values or metrics could be easily added for version updates or scheduled data adjustments. This allows updates to be made to the program without alterations to the program itself, rather, just to its sourced data file. 

## Versioning 

The design structure of this package acknowledges the need for updates to be made easily and efficiently. Due to the nature of the metrics calculated, it is important to make calculations with the most up-to-date metrics possible. For this reason, this package emphasizes the potential for versioning in its design. As stated previously, the main data source for executing calculations is a maintained data file that is easily updated to provide relevant and accurate calculation metrics. 

Beyond this, the package's potential to provide more functions in relation to international data preprocessing is evident. Conversions such as time-zone adjustments and percentage of global populations are just a few potential functions that could be added to this package in future versions using a similar structure and method.  

