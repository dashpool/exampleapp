import dash
from dash import html, register_page

register_page(__name__, path='/extra')

layout = html.Div([
    html.H1('This is an extra page.'),
])