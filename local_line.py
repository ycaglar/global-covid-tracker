"""
This is the 'local_line' module.

Local_line is essentially an interactive line graph. It displays new cases and
new deaths with two distinchtly colored lines and how they progressed within the
course of several months. The status summary window pops up on mouse hover. In
addition to that, the entire graph can be zoomed into by drawing a window with
the mouse.
"""

import plotly.express as px
from data_store import dataframe
import colors

def fig(country):
    df = dataframe
    df = df[df['Country'] == country]
    fig = px.line(df,
                  x = 'Date_reported',
                  y = ['New_cases', 'New_deaths'],
                  color_discrete_sequence = [colors.YlGnBu[4],
                                             colors.YlGnBu[6]],
                  labels = {'Date_reported':'Date Reported',
                            'value':'New Cases & New Deaths',
                            'variable':'Variables'},
                  title = f'{country} Status Report')
    fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
    return fig
