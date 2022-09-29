"""
This is the 'global_histogram' module.

The global_histogram module displays the progress of Covid-19 spread from a
regional perspective.
"""

import colors
import plotly.express as px
from data_store import dataframe as df

df = df[df['New_cases'] > 0]

fig = px.histogram(df,
                   x='Date_reported',
                   y='New_cases',
                   color='Region',
                   color_discrete_sequence=colors.YlGnBu[2:8],
                   hover_data=df.columns,
                   barmode='overlay',
                   labels={'New_cases': 'New Cases',
                           'Date_reported': 'Date Reported',
                           'WHO_region': 'Region'},
                   title='Progress History of New Cases by Region')
fig.update_layout(margin={'r': 0, 't': 60, 'l': 10, 'b': 10})
