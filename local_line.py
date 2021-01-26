import plotly.express as px
from data_store import dataframe

def fig(country):
    df = dataframe
    df = df[df['Country'] == country]
    df = df[df['New_cases'] > 4_000]
    fig = px.line(df,
                  x = 'Date_reported',
                  y = ['New_cases', 'New_deaths'],
                  labels = {'Date_reported':'Date Reported', 'value':'New Cases & New Deaths', 'variable':'Variables'},
                  title = f'{country} Status Report')
    fig.update_layout(margin = {'r':0,'t':60,'l':10,'b':10})
    return fig
