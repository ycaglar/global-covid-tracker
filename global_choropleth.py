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
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server


df = df[['Date_reported', 'Country', 'Country_code', 'Region', 'New_cases', 'Cumulative_cases', 'Cumulative_deaths']]
df = df.groupby(['Country', 'Country_code', 'Region', pd.Grouper(key='Date_reported', freq='M')]).agg({'New_cases':'sum', 'Cumulative_cases':'sum', 'Cumulative_deaths':'sum'}).reset_index()
df['Date_reported'] = df['Date_reported'].dt.strftime('%Y-%m')

# df = px.data.gapminder().query("year==2007")
# from dataframe_exporter import export
# export(df)

fig = px.choropleth(df,
                    locations='Country_code',
                    color="Cumulative_cases", # lifeExp is a column of gapminder
                    hover_name="Country", # column to add to hover information
                    hover_data=df.columns,
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.update_geos(projection_type="orthographic")
fig.update_layout(height=500, margin={"r":0,"t":10,"l":0,"b":10})


app.layout = html.Div([
    dcc.Graph(
        id='corona',
        figure=fig
    )
])


# Main
if __name__ == "__main__":
    app.run_server(debug=True)
