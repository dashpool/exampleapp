import os
from dash import html, dcc, callback, Output, Input, register_page
import dash_express_components as dxc
import plotly.express as px

# Generate a very long random variable
import numpy as np
long_random_variable = np.random.rand(10, 10).tolist()

import app.data as data


dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")
register_page(__name__, path='/plots')

layout = html.Div([
    html.H1(children='Example App', style={'textAlign':'center'}),
    dcc.Dropdown(data.df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    dcc.Graph(id='graph-too'),
    dcc.Store(id='long-random-variable-store', data=long_random_variable),

    dxc.Configurator(
            id="plotConfig",
            meta=data.df_meta,
            config = {'plot': {'type': 'box', 'params': {'x': 'continent', 'y': 'lifeExp'}}}
        ),
    dxc.Graph(
        id="fig",
        meta=data.df_meta,
        style={"height": "500px", "width": "100%"},
        longCallback=True,
    )
])

@callback(
    Output('graph-content', 'figure'),
    Output('graph-too', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value): 
    dff = data.df[data.df.country==value]
    return px.line(dff, x='year', y='pop'), px.scatter(dff, x='year', y='pop')

@callback(
    Output('fig', 'defParams'),
    Input('plotConfig', 'config'),
)
def update_config(newConfig):
    print("update_config", newConfig)
    return newConfig