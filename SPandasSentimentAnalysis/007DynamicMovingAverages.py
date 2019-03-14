import datetime
import pandas as pd
from pandas_datareader import data, wb
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')
pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as yf
yf.pdr_override()
import math


def outlier_fixing(stock_name):
    df = pd.read_csv('stocks_sentdex_dates_full.csv', index_col='time', parse_dates=True)

    df = df[df.type == stock_name.lower()]
    df['std'] = pd.rolling_std(df['close'], 25, min_periods=1)
    df = df[df['std'] < 20]

    ax1 = plt.subplot(2, 1, 1)
    df['close'].astype(float).plot(label='Price')
    plt.legend()

    ax2 = plt.subplot(2, 1, 2, sharex=ax1)
    df['std'].plot(label='Deviation')
    plt.legend()
    plt.show()

def single_stock_auto_MA(stock_name, div1=457, div2=304, div3=91, div4=45):
    df = pd.read_csv('stocks_sentdex_dates_full.csv', index_col='time', parse_dates=True)

    df = df[df.type == stock_name.lower()]
    count = df['type'].value_counts()

    count = int (count[stock_name])
    #print(count)

    MA1 = pd.rolling_mean(df['value'], round((count/div1)))
    MA2 = pd.rolling_mean(df['value'], round((count/div2)))
    MA3 = pd.rolling_mean(df['value'], round((count/div3)))
    MA4 = pd.rolling_mean(df['value'], round((count/div4)))

    # Series.rolling(window=100, center=False).mean()
    # MA1 = pd.rolling_mean(df['value'], round((count / div1)))
    # Series.rolling(window=151, center=False).mean()
    # MA2 = pd.rolling_mean(df['value'], round((count / div2)))
    # Series.rolling(window=503, center=False).mean()
    # MA3 = pd.rolling_mean(df['value'], round((count / div3)))
    # Series.rolling(window=1018, center=False).mean()
    # MA4 = pd.rolling_mean(df['value'], round((count / div4)))

    SP = int(math.ceil(count/div4))

    df['MA1'] =  MA1
    df['MA2'] =  MA2
    df['MA3'] =  MA3
    df['MA4'] =  MA4

    df =  df[SP:]

    ax1 = plt.subplot(2, 1, 1)
    df['close'].astype(float).plot(label='Price')

    ax2 = plt.subplot(2, 1, 2, sharex=ax1)
    # MA1.plot(label=(str(round(count/457))+ 'MA'))
    # MA2.plot(label=(str(round(count/304))+ 'MA'))
    # MA3.plot(label=(str(round(count/91))+ 'MA'))
    # MA4.plot(label=(str(round(count/45))+ 'MA'))

    df['MA1'].plot(label=(str(round(count/div1))+ 'MA'))
    df['MA2'].plot(label=(str(round(count/div2))+ 'MA'))
    df['MA3'].plot(label=(str(round(count/div3))+ 'MA'))
    df['MA4'].plot(label=(str(round(count/div4))+ 'MA'))

    plt.legend()
    plt.show()


single_stock_auto_MA('bac')

#single_stock_auto_MA('aapl')

#single_stock_auto_MA('goog')