import datetime
import pandas as pd
from pandas_datareader import data, wb
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as yf
yf.pdr_override()
import numpy as np

# start = datetime(2014, 6, 2)
# end = datetime(2014, 9, 5)
# google = web.DataReader('GOOG', 'google', start, end)
# tesla = web.DataReader('TSLA', 'google', start, end)
# apple = web.DataReader('AAPL', 'google', start, end)


#To get data:

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2012, 1, 1)
df = data.get_data_yahoo('MS', start, end)
sp500 = data.get_data_yahoo('%5EGSPC', start, end)
print(sp500.head())
sp500.to_csv('sp500_ohlc.csv')


df = pd.read_csv('sp500_ohlc.csv', index_col='Date', parse_dates=True)
#print(df.head())
#print(df.index)
# ts = df[['Close','Open', 'High']][-10:]
# print(ts)

# df['H-L'] = df.High - df.Low
# print(df.head())
# del df['H-L']
# print(df.head())


df['H-L'] = df.High - df.Low
close = df['Adj Close']
ma = pd.rolling_mean(close, 50)
# print (ma[-10:])

ax1 = plt.subplot(2, 1, 1)
ax1.plot(close, label='sp500')
ax1.plot(ma, label='50MA')
plt.legend()

ax2 = plt.subplot(2, 1, 2, sharex=ax1)
ax2.plot(df['H-L'], label='H-L')
plt.legend()
plt.show()