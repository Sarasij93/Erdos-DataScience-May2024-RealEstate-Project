#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("../data/Cleaned_data.csv")


# In[3]:


df["Age"] = 2024 - df['YEAR BUILT']
df['log_price'] = np.log(df['PRICE'])


# In[4]:


from sklearn.model_selection import train_test_split


# In[5]:


df_train, df_test = train_test_split(df.copy(), random_state = 123, test_size = 0.2)

df_train['Condo'] = 1*pd.get_dummies(df_train['PROPERTY TYPE'])['Condo/Co-op']
df_train['Single Family'] = 1*pd.get_dummies(df_train['PROPERTY TYPE'])['Single Family Residential']
df_train['Townhouse'] = 1*pd.get_dummies(df_train['PROPERTY TYPE'])['Townhouse']
df_train['Multi_Family4'] = 1*pd.get_dummies(df_train['PROPERTY TYPE'])['Multi-Family (2-4 Unit)']
df_train['Multi_Family5'] = 1*pd.get_dummies(df_train['PROPERTY TYPE'])['Multi-Family (5+ Unit)']


# In[6]:


from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV 
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold




# In[7]:


model = xgb.XGBRegressor()



df_test['Condo'] = 1*pd.get_dummies(df_test['PROPERTY TYPE'])['Condo/Co-op']
df_test['Single Family'] = 1*pd.get_dummies(df_test['PROPERTY TYPE'])['Single Family Residential']
df_test['Townhouse'] = 1*pd.get_dummies(df_test['PROPERTY TYPE'])['Townhouse']
df_test['Multi_Family4'] = 1*pd.get_dummies(df_test['PROPERTY TYPE'])['Multi-Family (2-4 Unit)']
df_test['Multi_Family5'] = 1*pd.get_dummies(df_test['PROPERTY TYPE'])['Multi-Family (5+ Unit)']

model.fit(df_train[['BEDS','BATHS', 'SQUARE FEET', 'LOT SIZE', 'zipcode', 'LATITUDE', 'LONGITUDE',
                      'Bayes_RatingSchool','crime_percentage', 'Age', 'Single Family', 'Townhouse', 'Condo', 'Multi_Family4', 'Multi_Family5']],
               df_train.log_price.values)

plt.figure(figsize=(16,7))

plt.hist(model.predict(df_test[['BEDS','BATHS', 'SQUARE FEET', 'LOT SIZE', 'zipcode', 'LATITUDE', 'LONGITUDE',
                      'Bayes_RatingSchool','crime_percentage', 'Age', 'Single Family', 'Townhouse', 'Condo', 'Multi_Family4', 'Multi_Family5']]),
           label='Predicted on Training', bins =100, hatch = '\\', alpha =0.6)

plt.hist(df_test.log_price.values, bins =100, alpha= 0.5)

plt.show()


# In[8]:

import joblib
joblib.dump(model, "rf_model.sav")


# In[14]:




