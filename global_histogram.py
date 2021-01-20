import copy
import pathlib
import urllib.request
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pprint
from dataframe import dataframe as df

app = dash.Dash(
    __name__, meta_tags=[{'name': 'viewport', 'content': 'width=device-width'}]
)
server = app.server

df = df[df['New_cases'] > 0]

d = df.groupby('Region')['New_cases'].apply(list).tolist()

fig = px.histogram(df,
                   x='Date_reported',
                   y='New_cases',
                   color='Region',
                   hover_data=df.columns,
                   barmode='overlay',
                   labels={'New_cases':'New Cases', 'Date_reported':'Date Reported', 'WHO_region':'Region'})


app.layout = html.Div([
    dcc.Graph(
        id='corona',
        figure=fig
    )
])


# Main
if __name__ == '__main__':
    app.run_server(debug=True)
