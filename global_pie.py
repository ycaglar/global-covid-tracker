import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')

app.layout = html.Div([
    dcc.Graph(
        id='corona',
        figure=fig
    )
])

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
