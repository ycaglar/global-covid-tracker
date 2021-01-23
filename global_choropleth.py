import pandas as pd
import plotly.express as px
from data_store import dataframe as df


df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
df = df[['Date_reported', 'Country', 'Country_code', 'Region', 'New_cases', 'Cumulative_cases', 'Cumulative_deaths']]
df['Date_reported'] = df['Date_reported'].dt.strftime('%Y-%m-%d')

fig = px.choropleth(df,
                    locations = 'Country_code',
                    color = 'New_cases',
                    hover_name = 'Country',
                    hover_data = ['Region', 'New_cases', 'Cumulative_cases', 'Cumulative_deaths'],
                    color_continuous_scale = px.colors.sequential.Plasma)
fig.update_geos(projection_type = 'orthographic')
fig.update_layout(height = 500, margin = {'r':0,'t':10,'l':0,'b':10})

fig.show()
