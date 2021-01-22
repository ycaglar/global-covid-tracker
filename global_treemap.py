from dataframe import dataframe as df
import plotly.express as px
import numpy as np
import pandas as pd

df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Country', 'Region', 'Cumulative_cases', 'Population']]


fig = px.treemap(df,
                 path = [px.Constant('World'), 'Region', 'Country'],
                 values = 'Population',
                 color = 'Cumulative_cases',
                 hover_data = ['Population', 'Cumulative_cases'])

fig.show()
