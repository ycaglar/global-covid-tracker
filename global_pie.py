"""
This is the 'global_pie' module.

The global_pie module displays the first 19 countries which were most impacted
by the Covid-19 global pandemic. First, the data imported from the data_store
module is grouped by countries and then sorted visualizing cumulative cases per
country  one function, factorial().  For example,

>>> factorial(5)
120
"""

import plotly.express as px
from data_store import dataframe as df
import colors
#from data_store import global_df as gdf

df = df[['Country', 'Cumulative_cases']]
df = df.groupby('Country').tail(1)

#df = df[df['Cumulative_cases'] / int(gdf['Cumulative_cases']) >= 0.011]
df.sort_values(by = ['Cumulative_cases'], inplace = True, ascending = False)
df = df[:19]

fig = px.pie(df,
             values = 'Cumulative_cases',
             names = 'Country',
             color_discrete_sequence = colors.YlGnBu_e[::-1],
             labels = {'Cumulative_cases':'Cumulative Cases'},
             title = 'Major Outbrakes Around the World')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
