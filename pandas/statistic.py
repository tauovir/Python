# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print (df)

# Sum

print(df.sum()) #Each individual column is added individually
print(df.sum(1))    # Axes
print(df.mean())    # 
print(df.std())    # Axes
# Methods Are
#count(),sum(),mean(),median(),mode(),std(),min(),max(),abs(),prod(),cumsum(),cumprod()
print(df.describe())

print(df.describe(include='number'))   # number,all,object
