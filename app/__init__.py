from dash import Dash, html, dcc, callback, Output, Input
import dash_express_components as dxc
import plotly.express as px
import json
from plotly.utils import PlotlyJSONEncoder
import pandas as pd
from flask import Flask, request
import os

dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df_meta = dxc.get_meta(df)

server = Flask(__name__)
app = Dash(__name__, server=server,
            external_stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"])

app.layout = html.Div([
    html.H1(children='Example App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),

    dxc.Configurator(
            id="plotConfig",
            meta=df_meta,
            config = {'plot': {'type': 'box', 'params': {'x': 'continent', 'y': 'lifeExp'}}}
        ),
    dxc.Graph(id="fig",
                   meta=df_meta, plotApi="plotApi",      style={"height": "500px", "width": "100%"}
                   )
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

@app.callback(
    Output('fig', 'defParams'),
    Input('plotConfig', 'config'),
)
def update_config(newConfig):
    print("update_config", newConfig)
    return newConfig


@app.server.route(dash_url_base_pathname + "plotApi", methods=['POST', 'GET'])
def plotApi():
    config = request.get_json()
    if request.method == 'POST':
        fig = dxc.get_plot(df, config)
        return json.dumps(fig, cls=PlotlyJSONEncoder)
    return {}

if __name__ == '__main__':
    app.run(debug=True)