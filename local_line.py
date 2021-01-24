import plotly.express as px
from data_store import dataframe as df

df = df[df['Country'] == 'United States']
df = df[df['New_cases'] > 4_000]

fig = px.line(df,
              x = 'Date_reported',
              y = ['New_cases', 'New_deaths'],
              labels = {'Date_reported':'Date Reported', 'value':'New Cases & New Deaths', 'variable':'Variables'})

fig.show()
