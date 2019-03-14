import quandl
import pandas as pd
import pickle
from matplotlib import pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt', 'r').read()

sub_df = pd.DataFrame()
usa_df = pd.DataFrame()
def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()
    #sub_df  = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        #df = df.pct_change()
        #print(df.columns.values)
        sub_df['Value'] = df['SA Value']
        sub_df['Value']= (sub_df['Value'] - sub_df['Value'][0]) / sub_df['Value'][0] * 100.0
        # print(sub_df['Value'].head())
        sub_df.rename(columns={'Value': abbv}, inplace=True)
        #main_df = sub_df
        # print(main_df.head())
        # print('************************')
        #df[abbv]= (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        # df['Value']= (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0

        #print(query)
        # print(df.head())
        # print(main_df.head())
        if main_df.empty:
            #main_df = df
            main_df = sub_df
            # print(main_df.head())
            # print('************************')
        else:
            # df.index.names = [abbv]
            # main_df = main_df.join(df)
            # main_df = main_df.join(df, lsuffix="_" + abbv)
            # df.rename(index={'Value_'+abbv : abbv})
            main_df = sub_df
            # print(main_df.head())
            # print('************************')

    # print(main_df.head())
    # # print('************************')
    pickle_out = open('pickle.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

    pickle_in = open('pickle.pickle', 'rb')
    HPI_data = pickle.load(pickle_in)

    HPI_data.to_pickle('pickle2.pickle')
    HPI_data2 = pd.read_pickle('pickle2.pickle')
    # print(HPI_data2.head())
    # print('************  HPI_data2 ************')

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    # print(df.columns.values)
    # print(df.head())
    usa_df['United States'] = df['SA Value']
    usa_df['United States'] = (usa_df['United States'] - usa_df['United States'][0]) / usa_df['United States'][0] * 100.0
    # df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    # print(usa_df.columns.values)
    # print(usa_df.head())
    return usa_df


# grab_initial_state_data()


fix = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('pickle.pickle')

TX1yr = HPI_data['TX'].resample('A', how='ohlc')
print(TX1yr)

HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI')
TX1yr.plot(ax= ax1)


plt.legend(loc=4)
plt.show()

