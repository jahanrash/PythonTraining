from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import datetime

yf.pdr_override()

stocks = ["APPL","GOOG"]
start = datetime.datetime(2012,5,31)
end = datetime.datetime(2018,3,1)

f = pdr.get_data_yahoo(stocks, start=start, end=end)
print(f.head())

print("***************************************************")



from yahoofinancials import YahooFinancials
import pandas as pd

# Select Tickers and stock history dates
ticker = 'AAPL'
ticker2 = 'MSFT'
ticker3 = 'INTC'
index = '^NDX'
freq = 'daily'
start_date = '2012-10-01'
end_date = '2017-10-01'


# Function to clean data extracts
def clean_stock_data(stock_data_list):
    new_list = []
    for rec in stock_data_list:
        if 'type' not in rec.keys():
            new_list.append(rec)
    return new_list

# Construct yahoo financials objects for data extraction
aapl_financials = YahooFinancials(ticker)
mfst_financials = YahooFinancials(ticker2)
intl_financials = YahooFinancials(ticker3)
index_financials = YahooFinancials(index)

# Clean returned stock history data and remove dividend events from price history
daily_aapl_data = clean_stock_data(aapl_financials
                                     .get_historical_stock_data(start_date, end_date, freq)[ticker]['prices'])
daily_msft_data = clean_stock_data(mfst_financials
                                     .get_historical_stock_data(start_date, end_date, freq)[ticker2]['prices'])
daily_intl_data = clean_stock_data(intl_financials
                                     .get_historical_stock_data(start_date, end_date, freq)[ticker3]['prices'])
daily_index_data = index_financials.get_historical_stock_data(start_date, end_date, freq)[index]['prices']
stock_hist_data_list = [{'NDX': daily_index_data}, {'AAPL': daily_aapl_data}, {'MSFT': daily_msft_data},
                        {'INTL': daily_intl_data}]


# Function to construct data frame based on a stock and it's market index
def build_data_frame(data_list1, data_list2, data_list3, data_list4):
    data_dict = {}
    i = 0
    for list_item in data_list2:
        if 'type' not in list_item.keys():
            data_dict.update({list_item['formatted_date']: {'NDX': data_list1[i]['close'], 'AAPL': list_item['close'],
                                                            'MSFT': data_list3[i]['close'],
                                                            'INTL': data_list4[i]['close']}})
            i += 1
    tseries = pd.to_datetime(list(data_dict.keys()))
    df = pd.DataFrame(data=list(data_dict.values()), index=tseries,
                      columns=['NDX', 'AAPL', 'MSFT', 'INTL']).sort_index()
    return df

print("***************************************************")

#Multiple stocks data at once example (returns list of JSON objects for each ticker):

from yahoofinancials import YahooFinancials

tech_stocks = ['AAPL', 'MSFT', 'INTC']
bank_stocks = ['WFC', 'BAC', 'C']

yahoo_financials_tech = YahooFinancials(tech_stocks)
yahoo_financials_banks = YahooFinancials(bank_stocks)

tech_cash_flow_data_an = yahoo_financials_tech.get_financial_stmts('annual', 'cash')
bank_cash_flow_data_an = yahoo_financials_banks.get_financial_stmts('annual', 'cash')

banks_net_ebit = yahoo_financials_banks.get_ebit()
tech_stock_price_data = tech_cash_flow_data.get_stock_price_data()

daily_bank_stock_prices = yahoo_financials_banks.get_historical_stock_data('2008-09-15', '2017-09-15', 'daily')

print("***************************************************")

yahoo_financials = YahooFinancials('WFC')
print(yahoo_financials.get_historical_stock_data("2017-09-10", "2017-10-10", "monthly"))


print("***************************************************")
