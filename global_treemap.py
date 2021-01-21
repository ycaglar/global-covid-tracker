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
import plotly.express as px


df = df[['Country', 'Region', 'Cumulative_cases']]
#df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.treemap(df,
                 path = [px.Constant('World'), 'Region', 'Country'],
                 values = 'Cumulative_cases')

fig.show()
