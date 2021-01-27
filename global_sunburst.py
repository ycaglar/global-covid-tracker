import pandas as pd
import plotly.express as px
from data_store import dataframe as df
from math import log

df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Country', 'Region', 'Cumulative_cases', 'Population']]
df = df[df['Population'] >= 30_000]


fig = px.sunburst(df,
                  path = ['Region', 'Country'],
                  values = 'Population',
                  color = df['Cumulative_cases'].apply(lambda cumulative_cases:log(cumulative_cases) if cumulative_cases > 1 else cumulative_cases),
                  color_continuous_scale = 'ylgnbu',
                  hover_data = ['Population', 'Cumulative_cases'],
                  labels = {'Cumulative_cases':'Cases', 'color':'Cases'},
                  title = 'Global Distribution of Cumulative Cases by Region')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
