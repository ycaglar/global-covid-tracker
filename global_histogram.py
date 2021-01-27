import plotly.express as px
from data_store import dataframe as df

df = df[df['New_cases'] > 0]

fig = px.histogram(df,
                   x = 'Date_reported',
                   y = 'New_cases',
                   color = 'Region',
                   color_discrete_sequence = ['#c7e9b4',
                                              '#7fcdbb',
                                              '#41b6c4',
                                              '#1d91c0',
                                              '#225ea8',
                                              '#253494'],
                   hover_data = df.columns,
                   barmode = 'overlay',
                   labels = {'New_cases':'New Cases', 'Date_reported':'Date Reported', 'WHO_region':'Region'},
                   title = 'Progress History of New Cases by Region')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
