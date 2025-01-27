# Erdos-DataScience-May2024-RealEstate-Project

### Team Members

Indupama Herath, Sarasij Maitra, Rafatu Salis, Ersin S&uuml;er



## Overview

Our primary goal is to predict housing prices for King County, WA, USA based on a number of features. We added some new features like school and crime rates for a given zip code.  We also built a small app on Streamlit that estimates housing price for a user who specifies the criteria in the app. 

## Stakeholders

- Families looking to settle down in King County, WA
- Real estate agents trying to give estimates to housing prices based on customer inputs like sqft, number of bed, baths, safety of neighbourhood, etc. 

## KPIs

- Get a baseline model of predicting the mean price and use root mean squared errors (rmse) to compare the performance of our models compared to the baseline.
- Get a good understanding of the key independent features that significantly affect house price.

  
## Dataset

- __Data Collection__
We used a data set that includes prices and features values of properties in King county, Washington, USA. The data sets were downloaded from the real estate property listing website [Redfin](https://www.redfin.com/county/118/WA/King-County).
In order to add school and crime ratings we used webscraping tools such as `beautifulSoup` on the websites [SchoolDigger](https://www.schooldigger.com/go/WA/county/King+County/search.aspx) and [CrimeGrade.org](https://crimegrade.org/crime-by-zip-code/).  


- __Data Description and Cleaning__
For each zipcode, we used [Bayesian Average](https://en.wikipedia.org/wiki/Bayesian_average) of the school ratings to have a good representation of the public schools in that location. We then added crime and school columns to the housing data. After filling out missing location values using other location data such as city and zip codes and dropping rows with missing values, the cleaned data set includes 4700 rows and 19 columns with 5 categorical variables and 14 numerical variables. The complete data sets are available under [data folder](https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/tree/FC-Trace-main/data) above.

- __Data Pre-Processing and Exploratory Data Analysis__
  - Include new features such as Age and log_price. Age = 2024 - YEAR BUILT, Log_price = log(PRICE)
  - Split the dataset into training and testing
  - Perform exploratory data analysis (eda) on training set to better understand the data set. The plots from the eda along with relevant comments are available under [EDA folder](https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/tree/FC-Trace-main/EDA) above. None of the variables seemed to exhibit an obvious correlation with `log_price`. The boxplot of the property type does seem to indicate that there is a dependency with the price.

<img width="665" height="400" alt="boxplot_property_type" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/45484654/ba306cfa-41fc-40f6-b918-1543f20baea7">

 <img width="509" alt="correlationheatmap" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/127027916/cfa6627a-422d-4a0f-9e5b-28bc586f7a01">

    
  - Identify features to be used in the models: We decided to use `BEDS, BATHS, SQUARE FEET, LOT SIZE, AGE, LATITUDE, LONGITUDE, Bayes_RatingSchool, crime_percentage, Age, zipcode, Property type (5 classes)` as our features for our models. 
  - prepare for modeling - we perform _One hot encoding_ on the categorical variable `PROPERTY_TYPE` so that the effect of this categorical variable is included in our models.
    
## Modeling approach:
- Baseline model - mean prices(in log scale)
- Advanced techniques:
  - K- Nearest Neighbors. 
  - Multiple linear regression 
  - Decision tree regressor
  - Random forest regressor
  - XGBoost regressor

<img width="533" alt="rmseall" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/127027916/e000baa8-34ab-4c64-86c0-57a21be4de0a">

Overall, all the models showed lower [Root Mean Squared Error (rmse)](https://en.wikipedia.org/wiki/Root_mean_square_deviation) compared to our baseline model; XGBoost model showed the best performance. We further explored the most significant features in this model. 

<img width="440" alt="featuresxgboost" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/127027916/fa1c64c3-8475-4223-93cf-6d10ed6f8903">


It is interesting to note the significant features in this model. Despite there being no strong correlation between Age and price, Age still contributes significantly to price determination, which is somewhat expected. Additionally, it makes sense that latitude and longitude have higher scores, as properties closer to commercial cities generally have higher prices compared to those further away. This relationship is effectively captured by these two features. Furthermore, school and crime ratings also play a crucial role in determining property prices, similar to the number of bedrooms and bathrooms.

By looking at the histograms of predicted prices versus actual prices on the testing set using the XGBoost model, we observed that while the model tended to underestimate the prices, it generally performed well in its predictions. 


<img width="602" alt="histogramxgboost" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/127027916/ecd9cfe7-d4c9-4fb3-9cf5-aa5f67ab9d3e">

To further evaluate the model we also looked at the qq-plot and residual plot. 


<img width="354" alt="qqplot" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/127027916/70cac537-ba3d-499f-8182-1c54088d11d5">

<img width="339" alt="residual" src="https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/assets/127027916/512068ec-4a46-4a9b-8023-64b8ab1b5bc9">

## Web Application

Using our final model, we built a simple web application on Streamlit that takes in user inputs (relvant to our model) and predicts the house price. The app is available at [King County Price Prediction App 2024](https://erdos-datascience-may2024-realestate-project-nevrbzjn2sh2zgsrc.streamlit.app/). We used modules such as folium to incorporate a map that shows nearby airports, big cities, etc. that hopefully gives a better idea of the desired location for the user. The relevant codes and files can be found under the [streamlit folder](https://github.com/Sarasij93/Erdos-DataScience-May2024-RealEstate-Project/tree/FC-Trace-main/streamlit) above. (Due to technical reasons, some of the files have been copied to the main git page also.)

## Conclusions
- Overall, all models did improve from the baseline model and did well on predicting the price.​

- Contribution of non-traditional features are similar to some of the traditional features.​
## Future Work
- Extend the study for other states.​​
- Incorporate more relevant features such as ​​
  - whether the house has experienced flooding, ​​
  - has mold issues, ​​
  - the quality of construction materials, ​​
  - the floor plan, and ​​
  - whether fixtures and appliances have been recently updated.​​
- Get more data corresponding to various property types over a significant period of time to understand the effect of time as well on real estate.

