import pandas as pd
import plotly.express as px
from data_store import dataframe as df
import colors


df = df[['Date_reported', 'Country', 'Region', 'New_cases', 'Cumulative_cases', 'Cumulative_deaths']]
df = df.groupby(['Country', 'Region', pd.Grouper(key = 'Date_reported', freq = 'M')]).agg({'New_cases':'sum', 'Cumulative_cases':'sum', 'Cumulative_deaths':'sum'}).reset_index()
df['Date_reported'] = df['Date_reported'].dt.strftime('%Y-%m')

fig = px.scatter(df,
                 x = 'Cumulative_cases',
                 y = 'Cumulative_deaths',
                 animation_frame = 'Date_reported',
                 animation_group = 'Country',
                 size = 'New_cases',
                 color = 'Region',
                 color_discrete_sequence = colors.YlGnBu[2:8],
                 hover_name = 'Country',
                 log_x = True,
                 log_y = True,
                 size_max = 100,
                 range_x = [50_000,7_000_000_00],
                 range_y = [5_00,5_000_000_00],
                 labels = {'Cumulative_cases':'Cumulative Cases',
                           'Cumulative_deaths':'Cumulative Deaths',
                           'Date_reported':'Date Reported',
                           'New_cases':'New Cases',},
                 title = 'Animated Progress History of Covid-19')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
