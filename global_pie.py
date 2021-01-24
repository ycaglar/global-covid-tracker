import plotly.express as px
from data_store import dataframe as df


df = df[['Country', 'Cumulative_cases']]
df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.pie(df,
             values = 'Cumulative_cases',
             names = 'Country',
             title = 'Major Outbrakes Around the World')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
