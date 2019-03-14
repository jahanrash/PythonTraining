import pandas_datareader as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()


pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as yf
yf.pdr_override()


stock = 'TSLA'
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2018, 2, 8)
df = web.get_data_yahoo(stock, start, end)
print(df.head(10))


# df = web.DataReader(stock, 'morningstar', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

app.layout = html.Div([
    html.H1(children='Whoa, a graph!'),

    html.Div('''
        Making a Stock graph!
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': df.index,
                 'y': df.Close,
                 'type': 'line',
                 'name': stock
                 }
            ],
            'layout': {
                'title':stock
            }
        }

    )


])

if __name__ == '__main__':
    app.run_server(debug=True)