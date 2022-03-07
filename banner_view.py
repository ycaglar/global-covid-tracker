import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    title = 'Global Covid Tracker',
    meta_tags = [{'name': 'viewport',
                  'content': 'width = device-width'}]
)

banner_view = html.Div(
        [
            html.Img(
                src = app.get_asset_url('banner.jpg'),
                #id="plotly-image",
                style={'width':'100%',
                       'height':'auto'},
            )
        ],
        style = { 'margin-top':'0' }
)
