"""
This is the 'global_treemap' module.

The treemap module uses boxes to visualize data. Each box represents a
geographic region or a sub-region. The outer most container is the World and the
other regions, continents, countries follow the same hierarchical structure by
nesting inside one another. Hover data provides a brief status report for each
section of the graph.
"""

from data_store import dataframe as df
import plotly.express as px
import pandas as pd
from math import log

df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Country', 'Region', 'New_cases', 'Population']]

fig = px.treemap(df,
                 custom_data = df.columns,
                 path = [px.Constant('World'), 'Region', 'Country'],
                 values = 'Population',
                 color = df['New_cases'].apply(lambda new_cases:log(new_cases) if new_cases > 1 else new_cases),
                 color_continuous_scale = 'ylgnbu',
                 #hover_data = ['Population', 'New_cases'],
                 labels = {'New_cases':'Cases', 'color':'Cases'},
                 title = 'Global Distribution of New Cases by Region')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
fig.update_traces(hovertemplate = 'Region: %{customdata[1]} <br>\
                                   Population: %{customdata[3]} <br>\
                                   New Cases: %{customdata[2]}')
