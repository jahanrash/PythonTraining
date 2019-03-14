import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np



style.use('ggplot')

web_stats = {
    'Day':[1, 2, 3, 4, 5, 6],
    'Visitors':[43, 34, 65, 56, 29, 76],
    'Bounce Rate':[65, 67, 78, 65, 45, 52]
}


df =  pd.DataFrame(web_stats)
print(df)
print("***************************************")
print(df.head())
print("***************************************")
print(df.tail())
print("***************************************")
print(df.tail(2))
print("***************************************")


df.set_index('Day', inplace=True)
print(df.head())
print("***************************************")
print(df['Visitors'])
print("***************************************")
print(df.Visitors)
print("***************************************")
print(df['Bounce Rate'])
print("***************************************")

#print(df['Bounce Rate','Visitors'])
print("***************************************")

print(df.Visitors.tolist())
print("***************************************")

print(np.array(df[['Bounce Rate','Visitors']]))

print("***************************************")
print("***************************************")
df2 = pd.DataFrame(np.array(df[['Bounce Rate', 'Visitors']]))
print(df2)

print("***************************************")

