# -*- coding: utf-8 -*-
"""
Created on Thu May 30 00:14:38 2024

@author: Owner
"""
# [1]:

import joblib
def predict(data):
    model = joblib.load("rf_model.sav")
    return model.predict(data)