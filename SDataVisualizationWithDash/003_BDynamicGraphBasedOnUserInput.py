import pandas_datareader as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output


# stock = 'TSLA'
# start = datetime.datetime(2015, 1, 1)
# end = datetime.datetime(2018, 2, 8)
# df = web.get_data_yahoo(stock, start, end)
# print(df.head(10))


# df = web.DataReader(stock, 'morningstar', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def update_value(input_data):
    pd.core.common.is_list_like = pd.api.types.is_list_like
    import fix_yahoo_finance as yf
    yf.pdr_override()
    start = datetime.datetime(2016, 1, 1)
    end = datetime.datetime(2018, 11, 8)
    df = web.get_data_yahoo(input_data, start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    # df = df.drop("Symbol", axis=1)
    print(df.head(10))

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)