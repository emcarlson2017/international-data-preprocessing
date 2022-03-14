# International Data Preprocessing

This Python package allows for the preprocessing of data frames that include international currency or populations. The motivation of this project is to provide a simplified process for normalizing global data so that it is more readable and accessible to the end users. This package is lightweight and is easily integrateable into current workflows. 

## Description

In order to properly analyze international data, it is necessary to undergo a process of normalization. This normalization process allows the end-users to make true comparisons of data values from one specific viewpoint, usually defined by country and year. This Python package allows end-users to complete this process by preparing data columns for function input, passing in a data frame and particular columns to a function, which will finally execute an intended calculation. Functionality includes adjusting currency for inflation by comparison year, converting international currency values using exchange rates, and providing per capita metrics using country populations by year. The design focuses on accessibility and ease of use, so that end-users may utilize this tool quickly and effectively. 

## Getting Started

In order to utilize this package, follow the installation instructions below. Once the package is available for use, data preprocessing can begin. First, users must ensure the data frame columns follow expected input guidelines before they are passed in to the function. Countries be in specified formats (alpha 3 codes) and currency types must be represented by their standard code (three letter currency code). Once this data has been prepared using the parsing functions made available through this package, the data is ready to be passed through the main package functions. Based on the desired output, select the appropriate functions and pass in the dataframe and the appropriate columns for calculation. More detail is provided on function input in the Functionality documentation.

### Installation

* ######################################################

### Executing program

The program can be executed using the following general steps: 

* Install package according to installation instructions 
* Load in pandas data frame for preprocessing 
* Outline goals for desired calculations or adjustments to ensure correct functionality is used 
* Parse data frame columns to match expected function input format 
* Execute desired functions to preprocess data frame columns 
* Ensure output meets desired goals and expectations 

Examples detailing how to execute the program according to these steps is shown in the Examples folder. An example of each function execution and parsing of input data is shown. 

## Help

For questions or concerns, reference the contact information below, or further explore the project and functionality documentation. 

## Authors

Shriraj Gandhi

Contact: ssgandhi@uw.edu

Emma Carlson 

Contact: emcar98@uw.edu

## Version History

Coming in 2023: Version 2.0

In January 2023, the international data preprocessing package will receive an update to its master data files in order to reflect the most relevant country populations, currency exchange rates, and inflation rates. This version will be the first of many updates in order to ensure that this package maintains its integrity and accuracy for every end user. 

## License

This project is licensed under the MIT License. See the LICENSE.md file for details

## Acknowledgments

* [readme-formatting] https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc
* [country-identifiers] https://www.un.int/protocol/sites/www.un.int/files/Protocol%20and%20Liaison%20Service/officialnamesofcountries.pdf
* [country-identifiers] https://www.nationsonline.org/oneworld/country_code_list.htm
