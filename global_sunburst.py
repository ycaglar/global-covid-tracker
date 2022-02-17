"""
This is the 'global_sunburst' module.

This module is an interactive graph designed to visualize the global data of the
distribution of cumulative cases by region. The graph has an inner and an outer
circle. The inner circle groups geographic regions and a pie slices branching
from the regions circle gives an idea of how each major sub-region was impacted.
Users can hover over the sections of the graph to see a brief status report and
they can also click on the geographic regions within the inner cicrcle to expand
the view and examine the status of the outbreak by focusing on a particular
region. 
"""

import pandas as pd
import plotly.express as px
from data_store import dataframe as df
from math import log

df = df[['Country', 'Region', 'Cumulative_cases', 'Population']]
df = df.groupby('Country').tail(1)
df.sort_values(by = ['Population'], inplace = True, ascending = False)
df = df[:30]

fig = px.sunburst(df,
                  custom_data = ['Country',
                                 'Region',
                                 'Population',
                                 'Cumulative_cases'],
                  path = ['Region', 'Country'],
                  values = 'Population',
                  color = df['Cumulative_cases'].apply(lambda cumulative_cases:log(cumulative_cases) if cumulative_cases > 1 else cumulative_cases),
                  color_continuous_scale = 'YlGnBu',
                  hover_data = ['Population', 'Cumulative_cases'],
                  labels = {'Cumulative_cases':'Cases', 'color':'Cases'},
                  title = 'Global Distribution of Cumulative Cases by Region')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
fig.update_traces(hovertemplate = '<b>%{customdata[0]}</b> <br>\
                                   Region: %{customdata[1]} <br>\
                                   Population: %{customdata[2]} <br>\
                                   Cumulative Cases: %{customdata[3]} <br>')
