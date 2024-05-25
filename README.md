# Erdos-DataScience-May2024-RealEstate-Project

### Team Members



## Overview

Our primary goal is to predict housing prices for King County, WA, USA based on a number of features. We added features like school and crime rates for a given zip code. 

 - If time permits, we will build a small app too that estimates housing price for a user who specifies the criteria in the app. 

The main techniques that we will use here for various model comparisons are:

-
-
-

## Dataset
- __Data Collection__ : We used the following websites for the respective data from King County, WA:

     1. For most zipcodes: [House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction); we added some more zipcodes to these.
     2. For public school ratings: [SchoolDigger](https://www.schooldigger.com/go/WA/county/King+County/search.aspx)
     3. For the real estate data: [Redfin](https://www.redfin.com/county/118/WA/King-County)
     4. For crime data: [CrimeGrade.org](https://crimegrade.org/crime-by-zip-code/)



- __Data Description__
      - The data set includes price for different real estate property types in King county, WA. There are 7031 rows and 29 columns in the raw data (pre-cleaning). Write a description of each columns after the data cleaning process. 

## Stakeholders

- Families looking to settle down in King County, WA
- Real estate agents trying to give estimates to housing prices based on customer inputs like sqft, number of bed, baths, saffety of neighbourhood, etc. 

## KPIs

- Get the mean price of houses in King County, WA using the data and use our models to compare with that.
- Get a baseline model of predicting the mean price and use our models to improve upton this.
- Get a good understanding of the key independent features that significantly affect house price.

## Data Collection 

- We used a data set that includes prices and features values of properties in King county, Washington, USA. The data sets were downloaded from the real estate property listing website [Redfin](https://www.redfin.com/county/118/WA/King-County).
- In order to add school and crime ratings we used the websites [SchoolDigger](https://www.schooldigger.com/go/WA/county/King+County/search.aspx) and [CrimeGrade.org](https://crimegrade.org/crime-by-zip-code/)
. 

## Data Description 
- After filling out missing location values using other location data such as city and zip codes and dropping rows with missing values, the cleaned data set includes 4700 rows and 19 columns with 5 categorical variables and 14 numerical variables. 
## Data Pre-Processing:
- Split the dataset into training and testing
- Perform exploratory data analysis on training set to better understand the data set 
- Identify features to be used in the model 
- prepare for modeling by scaling 
## Modeling approach:
- Baseline models - mean prices of the houses and K- Nearest Neighbors. 
- Advanced techniques:
- Multiple linear regression with feature set 1 
- Multiple linear regression with feature set 2
- Decision tree regressor
- Random forest regressor
- XGBoost regressor
- Neural Networks ?






## Conclusions

## Future Work


