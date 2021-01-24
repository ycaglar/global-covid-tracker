from data_store import dataframe as df
import plotly.express as px
import pandas as pd

df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Country', 'Region', 'New_cases', 'Population']]


fig = px.treemap(df,
                 path = [px.Constant('World'), 'Region', 'Country'],
                 values = 'Population',
                 color = 'New_cases',
                 hover_data = ['Population', 'New_cases'],
                 title = 'Global Distribution of New Cases by Region'
                 )
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
