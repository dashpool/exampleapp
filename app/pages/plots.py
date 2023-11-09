import os
from dash import html, dcc, callback, Output, Input, register_page
import dash_express_components as dxc
import plotly.express as px

import app.data as data


dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")
register_page(__name__, path=dash_url_base_pathname + 'plots')

layout = html.Div([
    html.H1(children='Example App', style={'textAlign':'center'}),
    dcc.Dropdown(data.df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),

    dxc.Configurator(
            id="plotConfig",
            meta=data.df_meta,
            config = {'plot': {'type': 'box', 'params': {'x': 'continent', 'y': 'lifeExp'}}}
        ),
    dxc.Graph(
        id="fig",
        meta=data.df_meta, plotApi=dash_url_base_pathname+"plotApi",
        style={"height": "500px", "width": "100%"}
    )
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value): 
    dff = data.df[data.df.country==value]
    return px.line(dff, x='year', y='pop')

@callback(
    Output('fig', 'defParams'),
    Input('plotConfig', 'config'),
)
def update_config(newConfig):
    print("update_config", newConfig)
    return newConfig