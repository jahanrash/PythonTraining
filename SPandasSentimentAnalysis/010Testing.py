import datetime
import pandas as pd
from pandas_datareader import data, wb
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
from matplotlib import style
style.use('ggplot')
pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as yf
yf.pdr_override()
import math
import time


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


def calc_position(ma1, ma2, ma3, ma4):
    if ma4 > ma1 > ma2 > ma3:
        return 1
    elif ma1 > ma4 > ma2 > ma3:
        return 2
    elif ma1 > ma2 > ma4 > ma3:
        return 3
    elif ma1 > ma2 > ma3 > ma4:
        return 4
    elif ma1 < ma2 < ma3 < ma4:
        return -4
    elif ma1 < ma2 < ma4 < ma3:
        return -3
    elif ma1 < ma4 < ma2 < ma3:
        return -2
    elif ma4 < ma1 < ma2 < ma3:
        return -1
    else:
        return None


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


    SP = int(math.ceil(count/div4))

    df['MA1'] = MA1
    df['MA2'] = MA2
    df['MA3'] = MA3
    df['MA4'] = MA4

    df = df[SP:]

    del df['MA100']
    del df['MA250']
    del df['MA500']
    del df['MA5000']

    df['Pos'] = map(calc_position, df['MA1'], df['MA2'], df['MA3'], df['MA4'])
    df['Change'] = df['Pos'].diff()

    #print(df[:200])
    #
    # ax1 = plt.subplot(2, 1, 1)
    # df['close'].astype(float).plot(label='Price')
    #
    # ax2 = plt.subplot(2, 1, 2, sharex=ax1)
    # # MA1.plot(label=(str(round(count/457))+ 'MA'))
    # # MA2.plot(label=(str(round(count/304))+ 'MA'))
    # # MA3.plot(label=(str(round(count/91))+ 'MA'))
    # # MA4.plot(label=(str(round(count/45))+ 'MA'))
    #
    # df['MA1'].plot(label=(str(round(count/div1))+ 'MA'))
    # df['MA2'].plot(label=(str(round(count/div2))+ 'MA'))
    # df['MA3'].plot(label=(str(round(count/div3))+ 'MA'))
    # df['MA4'].plot(label=(str(round(count/div4))+ 'MA'))
    #
    # plt.legend()
    # plt.show()
    return df


def backTest(datas, closei, changei):
    stockHoldings = 0
    startingCapital = datas['close'][0] * 8
    funds = startingCapital
    currentValuation = funds

    for row in datas.iterrows():
        try:
            index,data = row
            rowData = data.list()
            price = rowData[closei]
            change = int(rowData[closei])


            if isinstance(change, (int, long)) and change !=0:
                if change > 0:
                    if (change * price) < funds:
                        funds -= (change * price)
                        stockHoldings += change
                        currentValuation = funds + (stockHoldings * price)
                    else:
                        pass

                elif change < 0:
                    change = abs(change)

                    if stockHoldings == 0:
                        pass

                    elif (stockHoldings - change) < 0:
                        change = stockHoldings

                    else:
                        stockHoldings -=change
                        funds += (change * price)
                        currentValuation = funds + (stockHoldings * price)


        except:
            pass

    print('Holdings: ', stockHoldings)
    print('Funds: ', funds)
    print('Starting funds: ', startingCapital)
    print('Current Valuation: ', currentValuation)
    percChage = ((currentValuation - startingCapital) / startingCapital) * 100.00
    print('strategy Percent Growth:', percChage)



#city group
data = single_stock_auto_MA('c')
backTest(data, closei=3, changei=11)

#single_stock_auto_MA('aapl')

#single_stock_auto_MA('goog')