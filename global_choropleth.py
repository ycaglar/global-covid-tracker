import pandas as pd
import plotly.express as px
from data_store import dataframe as df
from math import log

df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Date_reported', 'Country', 'Country_code', 'Region', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']]
df['Date_reported'] = df['Date_reported'].dt.strftime('%Y-%m-%d')

fig = px.choropleth(df,
                    custom_data = ['Country', 'Region', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths'],
                    locations = 'Country_code',
                    color = df['New_cases'].apply(lambda new_cases:log(new_cases) if new_cases > 1 else new_cases),
                    color_continuous_scale = 'ylgnbu',
                    hover_name = 'Country',
                    hover_data = ['Region', 'New_cases', 'Cumulative_cases', 'Cumulative_deaths'],
                    labels = {'color':'New Cases'})
fig.update_geos(projection_type = 'orthographic')
fig.update_layout(margin = {'r':0,'t':10,'l':0,'b':10})
fig.update_traces(hovertemplate = '<b>%{customdata[0]}</b> <br>\
                                   Region: %{customdata[1]} <br>\
                                   New Cases: %{customdata[2]} <br>\
                                   Cumulative Cases: %{customdata[3]} <br>\
                                   New Deaths: %{customdata[4]} <br>\
                                   Cumulative Deaths: %{customdata[5]}')
