import dash
import dash_core_components as dcc
import dash_html_components as html
from global_choropleth import fig as global_choropleth

app = dash.Dash(
    __name__, meta_tags = [{'name': 'viewport', 'content': 'width = device-width'}]
)
server = app.server

# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id = 'aggregate_data'),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id = 'output-clientside'),
        html.Div(
            [
                html.Div(
                    [
                        html.Div([
                            html.H3('Live Status'),
                            html.H4('600,790'),
                            'New Cases',
                            html.H4('96,877,399'),
                            'Cumulative Cases',
                            html.H4('3,879'),
                            'New Deaths',
                            html.H4('2,098,879'),
                            'Cumulative Deaths'
                            ],
                            id = 'liveStatusContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    id = 'left-column',
                    className = 'three columns',
                    style = {'height':'100%'}
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'global_choropleth',
                                       figure = global_choropleth)],
                            id = 'globalChoroplethContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    id = 'right-column',
                    className = 'thirteen columns',
                )
            ],
            className = 'row flex-display',
        )
    ],
    id = 'mainContainer',
    style = {'display': 'flex', 'flex-direction': 'column'},
)

# Main
if __name__ == '__main__':
    app.run_server(debug = True)
