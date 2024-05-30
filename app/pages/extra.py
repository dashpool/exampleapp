import dash
import os
from dash import html, register_page, callback, Input, Output
import dash_express_components as dxc
import json

dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")
register_page(__name__, path='/extra')

layout = html.Div([
    html.H1('This is an extra long callback request state test.'),
    dxc.RequestStore(
        id="store",
        url=dash_url_base_pathname + "api",
        config={"dummy": 1},
        longCallback=True
    ),

    html.Pre([html.Code(id='output')]),

])


@callback(
    Output('output', 'children'),
    Input('store', 'data'),
)
def update_config(data):
    return json.dumps(data, indent=2)

