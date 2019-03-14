import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('homeprices.csv')
print(df)

print('******************************* Scatter plot ********************************')
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area, df.price, color='red', marker='+')
#plt.show()
print('*****************************************************************************')


area = df[['area']]
print(area)
print('*****************************************************************************')

price = df[['price']]
print(price)
print('*****************************************************************************')


print('*************************** Creating linear regression object ****************')
reg = linear_model.LinearRegression()
reg.fit(area, price)
print(reg)

print('--------------------------- predicting the price ----------------')
print(reg.predict(3300))

print('--------------------------- m value for y=mx + b ----------------')
print(reg.coef_)

print('--------------------------- b value for y=mx + b ----------------')
print(reg.intercept_)


print('--------------------------- Y value for y=mx + b when x = 3300 --')
print(((reg.coef_) * 3300) + reg.intercept_)


print('*************************** predicting list of the home price  ****************')
area_df = pd.read_csv("areas.csv")
print('-------printing area for first 5 rows------')
print(area_df.head())

p = reg.predict(area_df)
print('-------pricing for the listed areas  ------')
print(p)
area_df['prices'] = p
print('-------printing area and price for the  ------')
print(area_df)

print('------- save the area and predicted price into csv file  ------')
area_df.to_csv('prediction.csv')


print('*************************** creating the plot for the predicted price list of the home price  ****************')
plt.xlabel('area', fontsize=20)
plt.ylabel('price', fontsize=20)
plt.scatter(df.area, df.price, color='red', marker='+')
plt.plot(df.area, reg.predict(area), color='blue')
plt.show()

print('*************************** End of the linear regression  ****************')