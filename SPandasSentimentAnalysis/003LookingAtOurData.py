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


def modifyDataset():
    df = pd.read_csv('stocks_sentdex.csv')
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index('time')

    del df['id']
    #print(df.head())
    df.to_csv('stocks_sentdex_date_full.csv')


modifyDataset()