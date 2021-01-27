import plotly.express as px
from data_store import dataframe as df


df = df[['Country', 'Cumulative_cases']]
df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.pie(df,
             values = 'Cumulative_cases',
             names = 'Country',
             color_discrete_sequence = ['#c7e9b4',
                                        '#7fcdbb',
                                        '#41b6c4',
                                        '#1d91c0',
                                        '#225ea8',
                                        '#253494'],
             title = 'Major Outbrakes Around the World')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
