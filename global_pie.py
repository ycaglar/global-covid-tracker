import plotly.express as px
from data_store import dataframe as df
import colors

df = df[['Country', 'Cumulative_cases']]
df = df[df['Cumulative_cases'] >= 1_000_000]

fig = px.pie(df,
             values = 'Cumulative_cases',
             names = 'Country',
             color_discrete_sequence = colors.YlGnBu,
             title = 'Major Outbrakes Around the World')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
