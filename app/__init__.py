from dash import Dash, html, page_container
import dash_express_components as dxc
import json
from plotly.utils import PlotlyJSONEncoder
from flask import Flask, request, make_response
import datetime
import os
import time

import app.data as data



dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")


server = Flask(__name__)
app = Dash(__name__, server=server,
            external_stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"],
            use_pages=True,
            url_base_pathname=dash_url_base_pathname
)

app.layout = html.Div(page_container)

@app.server.route(dash_url_base_pathname + "plotApi", methods=['POST', 'GET'])
def plotApi():
    config = request.get_json()
    time.sleep(20.0)   
    if request.method == 'POST':
        fig = dxc.get_plot(data.df, config)

        # Create a response with an "Expires" header set to 15 minutes (900 seconds)
        response = make_response(json.dumps(fig, cls=PlotlyJSONEncoder))
        response.headers['Expires'] = (datetime.datetime.now() + datetime.timedelta(seconds=900)).strftime('%a, %d %b %Y %H:%M:%S GMT')
        
        return response
    return {}

if __name__ == '__main__':
    app.run(debug=True)