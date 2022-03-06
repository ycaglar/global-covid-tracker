import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    title = 'Global Covid Tracker',
    meta_tags = [{'name': 'viewport',
                  'content': 'width = device-width'}]
)

live_status = html.Div(
    [
        html.Div([
            html.Div(
                [
                    html.H3('Live Status')
                ],
                style = {'margin-bottom':'15%',
                         'text-align':'center'}
            ),
            html.H4(global_df['New_cases']),
            'New Cases',
            html.H4(global_df['Cumulative_cases']),
            'Cumulative Cases',
            html.H4(global_df['New_deaths']),
            'New Deaths',
            html.H4(global_df['Cumulative_deaths']),
            'Cumulative Deaths'
            ],
            id = 'liveStatusContainer',
            className = 'pretty_container',
            style = {'height': '100%',
                     'color':'#373737',
                     'text-align':'right'},
        ),
    ],
    id = 'left-column',
    className = 'three columns'
)
