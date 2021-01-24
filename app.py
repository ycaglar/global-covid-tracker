import dash
import dash_core_components as dcc
import dash_html_components as html
from global_choropleth import fig as global_choropleth
from global_treemap import fig as global_treemap
from global_histogram import fig as global_histogram
from global_progress import fig as global_progress
from global_sunburst import fig as global_sunburst
from global_pie import fig as global_pie

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
                    className = 'three columns'
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
                    className = 'ten columns',
                )
            ],
            className = 'row flex-display',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'global_treemap',
                                       figure = global_treemap)],
                            id = 'globalTreemapContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    id = 'single-column-treemap',
                    className = 'twelve columns',
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'global_histogram',
                                       figure = global_histogram)],
                            id = 'globalHistogramContainer',
                            className = 'pretty_container',
                        )
                    ],
                    id = 'single-column-histogram',
                    className = 'twelve columns',
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'global_progress',
                                       figure = global_progress)],
                            id = 'globalProgressContainer',
                            className = 'pretty_container',
                        )
                    ],
                    id = 'single-column-progress',
                    className = 'twelve columns',
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'global_sunburst',
                                       figure = global_sunburst)],
                            id = 'globalSunburstContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    #id = 'left-column-sunburst',
                    className = 'six columns'
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'global_pie',
                                       figure = global_pie)],
                            id = 'globalPieContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    #id = 'right-column-pie',
                    className = 'six columns',
                )
            ],
            className = 'row flex-display',
        ),
    ],
    id = 'mainContainer',
    style = {'display': 'flex', 'flex-direction': 'column'},
)

# Main
if __name__ == '__main__':
    app.run_server(debug = True)
