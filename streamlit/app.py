# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:05:48 2024

@author: Owner
"""

import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

df = pd.read_csv('../data/Cleaned_data.csv')
zip_options = np.sort(np.unique(df['zipcode'].values))




st.title('Predict House Price in King County, WA, USA')
st.markdown('Basic Real Estate Prediction using Advanced Regression Techniques')
st.markdown('The user inputs required are __property type, zipcode, latitude, longitude, age of house, beds, baths, sqft, lot size__')
      
#col1, col2 = st.columns(2)  
#with col1:   
types = np.unique(df['PROPERTY TYPE'].values)

property_type = st.selectbox('Enter desired Property Type', types)

st.write('_Property type chosen by user:_', str(property_type))
        


#with col2:
    
zipcode = st.selectbox('Choose your desired zipcode', zip_options)
def lat_range(zipcode):
    return np.sort(np.unique(df.loc[df['zipcode'] == zipcode].LATITUDE.values))



def long_range(zipcode):
    return np.sort(np.unique(df.loc[df['zipcode'] == zipcode].LONGITUDE.values))
if zipcode:
    st.write('__The map below shows the available latitudes and longitudes for all property types from Redfin for zipcode__', zipcode)


if zipcode:
    data = pd.DataFrame({'LATITUDE':lat_range(zipcode),
                         'LONGITUDE':long_range(zipcode)})
    #Lati = lat_range(zipcode)
    #Longi = long_range(zipcode)
    #points = [(Lati[i],Longi[i]) for i in range(len(lat_range(zipcode)))]
    #m=None
    #for point in points:
     #   m = folium.Map(location = point)
      #  folium.Marker(location = point).add_to(m)
    #st_folium(m)
    st.map(data)
        
st.write('__Please select latitude and longitude of the location you are interested in. The map below will point the precise location.__')
        
if zipcode:
    latitude = st.select_slider('Enter Latitude', lat_range(zipcode))
    longitude = st.select_slider('Enter Latitude', long_range(zipcode))
    
if latitude and longitude:
    st.write('Chosen Latitude and Longitude', (latitude, longitude))
    spec=pd.DataFrame({'LATITUDE':latitude,
                      'LONGITUDE':longitude,
                      'index':[0]})
    maps = folium.Map(location = (latitude,longitude))
    folium.Marker(location = (latitude,longitude), popup = 'Your Choice').add_to(maps)
    st_folium(maps)
    
age = st.slider('Enter age of house', 0, 131)
    
st.write('_Desired age of house:_', age)
    
beds = st.slider('Enter number of beds', 0, 41)
    
st.write('_Desired number of bedrooms:_', beds)
    
baths = st.slider('Enter number of baths', 0, 52)
    
st.write('_Desired number of bathrooms:_', baths)
    
    
sqft = st.slider('Enter desired square footage of the entire house interior', 
                     0.0, 34020.00)
    
st.write('_Desired livable square footage:_', sqft)
    
    
lotsize = st.slider('Enter desired Lot size of the land', 0.0, 2356708.0)
    
st.write('_Desired lotsize:_', lotsize)





if zipcode:
    crime_percentage = np.unique(df.loc[df['zipcode'] == zipcode].crime_percentage.values)[0]
    Bayes_RatingSchool = np.unique(df.loc[df['zipcode'] == zipcode].Bayes_RatingSchool.values)[0]

if zipcode:
    if property_type:
        if property_type == 'Condo/Co-op':
            features = [beds, baths, sqft, lotsize, zipcode, latitude, longitude,
                        Bayes_RatingSchool, crime_percentage, age, 0, 0, 1, 0, 0]
        elif property_type == 'Multi-Family (2-4 Unit)':
            features = [beds, baths, sqft, lotsize, zipcode, latitude, longitude,
                        Bayes_RatingSchool, crime_percentage, age, 0, 0, 0, 1, 0]
        elif property_type == 'Multi-Family (5+ Unit)':
            features = [beds, baths, sqft, lotsize, zipcode, latitude, longitude,
                        Bayes_RatingSchool, crime_percentage, age, 0, 0, 0, 0, 1]
        elif property_type == 'Single Family Residential':
            features = [beds, baths, sqft, lotsize, zipcode, latitude, longitude,
                        Bayes_RatingSchool, crime_percentage, age, 1, 0, 0, 0, 0]
        elif property_type == 'Townhouse':
            features = [beds, baths, sqft, lotsize, zipcode, latitude, longitude,
                        Bayes_RatingSchool, crime_percentage, age, 0, 1, 0, 0, 0]
        else:
            features = [beds, baths, sqft, lotsize, zipcode, latitude, longitude,
                        Bayes_RatingSchool, crime_percentage, age, 0, 0, 0, 0, 0]    





from prediction import predict


if st.button("Predict price of house"):
    result = np.power(2.718281, predict([features]))
    st.write('## Predicted price is $', result[0])
else: 
    print ("Not all values are selected")
    



