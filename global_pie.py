import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dataframe import dataframe as df


df = df[['Country', 'Cumulative_cases']]
df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.pie(df,
             values = 'Cumulative_cases',
             names = 'Country',
             title = 'Highest cumulative cases worldwide')

fig.show()
