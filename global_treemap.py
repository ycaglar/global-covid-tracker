from dataframe import dataframe as df
import plotly.express as px


df = df[['Country', 'Region', 'Cumulative_cases']]
#df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.treemap(df,
                 path = [px.Constant('World'), 'Region', 'Country'],
                 values = 'Cumulative_cases')

fig.show()
