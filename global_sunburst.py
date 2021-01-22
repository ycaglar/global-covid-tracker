import datetime as dt
import pandas as pd
import plotly.express as px
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
