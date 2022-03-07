import dash
from dash import html, dcc
from covid_data_global import df as global_df
from global_choropleth import fig as global_choropleth


app = dash.Dash(
    __name__,
    title = 'Global Covid Tracker',
    meta_tags = [{'name': 'viewport',
                  'content': 'width = device-width'}]
)

global_choropleth_view = html.Div(
    [
        html.Div(
            [dcc.Graph(id = 'global_choropleth',
                       figure = global_choropleth)],
            id = 'globalChoroplethContainer',
            className = 'pretty_container',
        ),
    ],
    id = 'right-column',
    className = 'ten columns',
)
