import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from global_choropleth import fig as global_choropleth
from global_treemap import fig as global_treemap
from global_histogram import fig as global_histogram
from global_progress import fig as global_progress
from global_sunburst import fig as global_sunburst
from global_pie import fig as global_pie
from local_line import fig as local_line
from data_store import dataframe as df
from data_store import global_df

app = dash.Dash(
    __name__, meta_tags = [{'name': 'viewport', 'content': 'width = device-width'}]
)
server = app.server

country_options = [{"label": country, "value": country}
                    for country in df[df['Cumulative_cases'] > 4_000]['Country'].drop_duplicates()]

# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id = 'aggregate_data'),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id = 'output-clientside'),
        html.Div(
            [
                html.Img(
                    src = app.get_asset_url('banner_module.jpg'),
                    #id="plotly-image",
                    style={'width':'100%',
                           'height':'auto'},
                )

            ],
            style = { 'margin-top':'0' }
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div([
                            html.Div(
                                [
                                    html.H3('Live Status')
                                ],
                                style = {'margin-bottom':'15%', 'text-align':'center'}
                            ),
                            html.H4(global_df['New_cases']),
                            'New Cases',
                            html.H4(global_df['Cumulative_cases']),
                            'Cumulative Cases',
                            html.H4(global_df['New_deaths']),
                            'New Deaths',
                            html.H4(global_df['Cumulative_cases']),
                            'Cumulative Deaths'
                            ],
                            id = 'liveStatusContainer',
                            className = 'pretty_container',
                            style = {'height': '100%', 'color':'#373737', 'text-align':'right'},
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
                            html.Label('Country'),
                                dcc.Dropdown(
                                    id = 'local_line_input',
                                    options = country_options,
                                    value = 'United States'
                                )
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
                            [dcc.Graph(id = 'local_line_output')],
                            id = 'localLineContainer',
                            className = 'pretty_container',
                        ),
                    ],
                    id = 'right-column-local-line',
                    className = 'eleven columns',
                )
            ],
            className = 'row flex-display',
        )
    ],
    id = 'mainContainer',
    style = {'display':'flex', 'flex-direction':'column', 'margin-top':'0'},
)

@app.callback(
    Output(component_id='local_line_output', component_property='figure'),
    Input(component_id='local_line_input', component_property='value')
)
def update_output_div(input_value):
    return local_line(input_value)

# Main
if __name__ == '__main__':
    app.run_server(debug = True)
