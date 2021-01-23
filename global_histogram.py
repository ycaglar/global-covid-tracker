import plotly.express as px
from data_store import dataframe as df


df = df[df['New_cases'] > 0]

fig = px.histogram(df,
                   x = 'Date_reported',
                   y = 'New_cases',
                   color = 'Region',
                   hover_data = df.columns,
                   barmode = 'overlay',
                   labels = {'New_cases':'New Cases', 'Date_reported':'Date Reported', 'WHO_region':'Region'})

fig.show()
