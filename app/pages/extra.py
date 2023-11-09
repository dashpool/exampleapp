import dash
from dash import html, register_page
import os

dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")
register_page(__name__, path=dash_url_base_pathname + 'extra')

layout = html.Div([
    html.H1('This is an extra page.'),
])