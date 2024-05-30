# Erdos-DataScience-May2024-RealEstate-Project

### Team Members



## Overview

Our primary goal is to predict housing prices for King County, WA, USA based on a number of features. We added features like school and crime rates for a given zip code. 

 - If time permits, we will build a small app too that estimates housing price for a user who specifies the criteria in the app. 

## Stakeholders

- Families looking to settle down in King County, WA
- Real estate agents trying to give estimates to housing prices based on customer inputs like sqft, number of bed, baths, saffety of neighbourhood, etc. 

## KPIs

- Get the mean price of houses in King County, WA using the data and use our models to compare with that.
- Get a baseline model of predicting the mean price and use our models to improve upton this.
- Get a good understanding of the key independent features that significantly affect house price.

  
## Dataset

- __Data Collection__
We used a data set that includes prices and features values of properties in King county, Washington, USA. The data sets were downloaded from the real estate property listing website [Redfin](https://www.redfin.com/county/118/WA/King-County).
In order to add school and crime ratings we used the websites [SchoolDigger](https://www.schooldigger.com/go/WA/county/King+County/search.aspx) and [CrimeGrade.org](https://crimegrade.org/crime-by-zip-code/)
. 

- __Data Description__
After filling out missing location values using other location data such as city and zip codes and dropping rows with missing values, the cleaned data set includes 4700 rows and 19 columns with 5 categorical variables and 14 numerical variables.
- __Data Cleaning__
- __Data Pre-Processing__
  - Include new features such as Age and log_price. Age = 2024 - YEAR BUILT, Log_price = log(PRICE)
  - Split the dataset into training and testing
  - Perform exploratory data analysis on training set to better understand the data set 
  - Identify features to be used in the model: We decided to use BEDS, BATHS, SQUARE FEET, LOT SIZE, AGE, LATITUDE, LATITUDE, Bayes_RatingSchool, crime_percentage, Age, zipcode, Property type (5 classes)
  - prepare for modeling - One hot encoding on the categorical variable PROPERTY_TYPE. 
## Modeling approach:
- Baseline models - mean prices(in log scale)
- Advanced techniques:
  - K- Nearest Neighbors. 
  - Multiple linear regression 
  - Decision tree regressor
  - Random forest regressor
  - XGBoost regressor






## Conclusions

## Future Work


