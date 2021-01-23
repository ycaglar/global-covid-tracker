import plotly.express as px
from data_store import dataframe as df


df = df[['Country', 'Cumulative_cases']]
df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.pie(df,
             values = 'Cumulative_cases',
             names = 'Country',
             title = 'Highest cumulative cases worldwide')

fig.show()
