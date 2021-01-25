import pandas as pd
import plotly.express as px
from data_store import dataframe as df

df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Country', 'Region', 'Cumulative_cases', 'Population']]
df = df[df['Population'] >= 30_000]


fig = px.sunburst(df,
                  path = ['Region', 'Country'],
                  values = 'Population',
                  color = 'Cumulative_cases',
                  hover_data = ['Population', 'Cumulative_cases'],
                  labels = {'Cumulative_cases':'Cases'},
                  title = 'Global Distribution of Cumulative Cases by Region')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
