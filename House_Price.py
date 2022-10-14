# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:40:24 2022

@author: Shalin_015
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv(r'F:\Work\IAR\SEM-6\ML\Practical\House price prediction using linear regression\Dataset.csv')
print(dataset)

print(dataset.shape)
print(dataset.head(5))

plt.xlabel('area')
plt.ylabel('price')
plt.scatter(dataset.area, dataset.price, color='purple', marker='*')

x=dataset.drop('price', axis='columns')
print(x)

y=dataset.price
print(y)

model = LinearRegression()
model.fit(x,y)

x = 40000
LandAreainSqFt=[[x]]
PredictedmodelResult = model.predict(LandAreainSqFt)
print(PredictedmodelResult)

m = model.coef_
print(m)

b = model.intercept_
print(b)

y = m * x + b

print("The price of {0} Sqaure Feet Land is : {1}".format(x,y[0])) 