import plotly.express as px
from data_store import dataframe as df
import colors
#from data_store import global_df as gdf

df = df[['Country', 'Cumulative_cases']]
df = df.groupby('Country').tail(1)

#df = df[df['Cumulative_cases'] / int(gdf['Cumulative_cases']) >= 0.011]
df.sort_values(by = ['Cumulative_cases'], inplace = True, ascending = False)

fig = px.pie(df[:19],
             values = 'Cumulative_cases',
             names = 'Country',
             color_discrete_sequence = colors.YlGnBu_e[::-1],
             title = 'Major Outbrakes Around the World')
fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
