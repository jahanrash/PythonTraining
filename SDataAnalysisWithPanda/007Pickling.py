import quandl
import pandas as pd
import pickle

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt', 'r').read()


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()
    sub_df  = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken=api_key, index='Date')
        # print(query)
        # print(df.columns.values)
        # print(df.head())
        # # print(main_df.head())
        if main_df.empty:
            sub_df['Value'] = df['SA Value']
            sub_df.rename(columns={'Value': abbv}, inplace=True)
            main_df = sub_df
            # print(main_df.head())
            # print('************************')

        else:
            sub_df['Value'] = df['SA Value']
            sub_df.rename(columns={'Value': abbv}, inplace=True)
            main_df = sub_df
            # print(main_df.head())
            # print('************************')

    # print(main_df.head())
    # print('************************')
    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

    pickle_in = open('fiddy_states.pickle', 'rb')
    HPI_data = pickle.load(pickle_in)
    # print(HPI_data)

    HPI_data.to_pickle('pickle.pickle')
    HPI_data2 = pd.read_pickle('pickle.pickle')
    print(HPI_data2)

grab_initial_state_data()