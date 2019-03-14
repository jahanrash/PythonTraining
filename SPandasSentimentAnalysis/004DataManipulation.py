import datetime
import pandas as pd
from pandas_datareader import data, wb
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')
pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as yf
yf.pdr_override()


def single_stock(stock_name):
    df = pd.read_csv('stocks_sentdex_dates_full.csv', index_col='time', parse_dates=True)

    df = df[df.type == stock_name.lower()]

    _500MA = pd.rolling_mean(df['value'], 500)

    ax1 = plt.subplot(2, 1, 1)
    df['close'].astype(float).plot(label='Price')
    plt.legend()

    ax2 = plt.subplot(2, 1, 2, sharex=ax1)
    _500MA.plot(label='500MA')
    plt.legend()

    plt.show()


single_stock('bac')