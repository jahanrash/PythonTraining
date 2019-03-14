import pandas as pd
import numpy as np
from sklearn import linear_model
import math


print('*********************** read the homepirces.csv file******************')
df =  pd.read_csv('homeprices.csv')
print(df)



print('***********************  Replace NaN variables with median ******************')
med_bedrooms = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(med_bedrooms)
print(df)


print('***********************  Creating the model ******************')
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)
print('------------printing the model the model')
print(reg)
print('------------printing the coefficient')
print(reg.coef_)
print(reg.intercept_)


print('***********************  predicting the price  ******************')
print(reg.predict([[3000, 3, 40]]))
print('------------calculation')
print(((reg.coef_[0])* 3000) + ((reg.coef_[1]) * 3) + ((reg.coef_[2])*40) + reg.intercept_ )


print('*************************** End of the linear regression  ****************')

