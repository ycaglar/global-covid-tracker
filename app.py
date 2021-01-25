import dash
import dash_core_components as dcc
import dash_html_components as html
from global_choropleth import fig as global_choropleth
from global_treemap import fig as global_treemap
from global_histogram import fig as global_histogram
from global_progress import fig as global_progress
from global_sunburst import fig as global_sunburst
from global_pie import fig as global_pie
from local_line import fig as local_line

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
        html.H1('GLOBAL COVID TRACKER'),
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
                            style = {'height': '100%'},
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
                            className = 'pretty_container'
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
                    id = 'small-column-sunburst',
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
                    id = 'small-column-pie',
                    className = 'six columns',
                )
            ],
            className = 'row flex-display',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div([
                            html.Label('Dropdown'),
                                dcc.Dropdown(
                                    options=[
                                        {'label': 'New York City', 'value': 'NYC'},
                                        {'label': u'Montréal', 'value': 'MTL'},
                                        {'label': 'San Francisco', 'value': 'SF'}
                                    ],
                                    value='MTL'
                                ),
                            html.Label('Radio Items'),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'New York City', 'value': 'NYC'},
                                        {'label': u'Montréal', 'value': 'MTL'}
                                    ],
                                    value='MTL'
                                ),
                            html.Label('Slider'),
                                dcc.Slider(
                                    min=0,
                                    max=9,
                                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                                    value=5,
                                ),
                            ],
                            id = 'localTweakContainer',
                            className = 'pretty_container',
                            style = {'height': '90%'},
                        ),
                    ],
                    id = 'left-column-local-tweak',
                    className = 'four columns'
                ),
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id = 'local_line',
                                       figure = local_line)],
                            id = 'localLineContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    id = 'right-column-local-line',
                    className = 'eleven columns',
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
