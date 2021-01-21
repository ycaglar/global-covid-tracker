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

df = df[['Date_reported', 'Country', 'Region', 'New_cases', 'Cumulative_cases', 'Cumulative_deaths']]
df = df.groupby(['Country', 'Region', pd.Grouper(key = 'Date_reported', freq = 'M')]).agg({'New_cases':'sum', 'Cumulative_cases':'sum', 'Cumulative_deaths':'sum'}).reset_index()
df['Date_reported'] = df['Date_reported'].dt.strftime('%Y-%m')


df = px.data.gapminder().query('year == 2007')
fig = px.sunburst(df,
                  path = ['continent', 'country'],
                  values = 'pop',
                  color = 'lifeExp',
                  hover_data = ['iso_alpha'])

fig.show()
