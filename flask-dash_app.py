import sys, os
from flask import Flask, render_template
from flask_flatpages import FlatPages
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import geopandas as gpd
from shapely.geometry import LineString, MultiLineString
import numpy as np
from shapefile_to_geojson import shapefile_to_geojson

server = Flask(__name__)
server.config.from_object(__name__)
pages = FlatPages(server)
FLATPAGES_EXTENSION = '.md'
server.url_map.strict_slashes = False

@server.route("/")
def index():
    return render_template('index.html', pages=pages)

@server.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)

@server.route("/software")
def software():
    return render_template('software.html')

@server.route("/airpollution")
def airpollution():
    return render_template('airpollution.html')


# dash app
mapboxt = open("/nfs/see-fs-02_users/earlacoa/.mapbox_token").read().rstrip()

level = 1
gdf = gpd.read_file('/nfs/a68/earlacoa/shapefiles/india_new/gadm36_IND_' + str(level) +'.shp', encoding='utf-8')
# remove superfluous states
gdf.drop(5, inplace=True)
gdf.drop(17, inplace=True)
gdf.reset_index(inplace=True)
del gdf['index']
geojsdata = shapefile_to_geojson(gdf, list(gdf.index))

appended_df = []
appended_format_df = []
scenarios = ['BASELINE', 'ALLLPG', 'URB15', 'EMIS50', 'STATE50']
for scenario in scenarios:
    df = pd.read_csv('/nfs/a336/earlacoa/paper_erl_india_sfi/supp-data_' + scenario + '.csv')[0:34]
    df.rename(columns={'Unnamed: 0':'geo-id'}, inplace=True)
    df['scenario'] = scenario
    appended_df.append(df)

for scenario in scenarios:
    df = pd.read_csv('/nfs/a336/earlacoa/paper_erl_india_sfi/supp-data_' + scenario + '.csv')
    format_data = [("Ambient PM\u2082.\u2085 concentration", 'apm25_popweighted', 0, 100, '0,0', 'Ambient ' + u'PM\u2082.\u2085' + ' concentration (India = ' + str(df.apm25_popweighted.values[-1]) + ' ' + u'\u03bcg' + '/' + u'm\u00b3' + ")"),
               ("Household PM\u2082.\u2085 concentration, females", 'hpm25_female_popweighted', 0, 300, '0,0', 'Household ' + u'PM\u2082.\u2085' + ' concentration, females (India = ' + str(df.hpm25_female_popweighted.values[-1]) + ' ' + u'\u03bcg' + '/' + u'm\u00b3' + ')'),
               ("Household PM\u2082.\u2085 concentration, males", 'hpm25_male_popweighted', 0, 300, '0,0', 'Household ' + u'PM\u2082.\u2085' + ' concentration, males (India = ' + str(df.hpm25_male_popweighted.values[-1]) + ' ' + u'\u03bcg' + '/' + u'm\u00b3' + ')'),
               ("Household PM\u2082.\u2085 concentration, children", 'hpm25_child_popweighted', 0, 300, '0,0', 'Household ' + u'PM\u2082.\u2085' + ' concentration, children (India = ' + str(df.hpm25_child_popweighted.values[-1]) + ' ' + u'\u03bcg' + '/' + u'm\u00b3' + ')'),
               ("MORT from total PM\u2082.\u2085 exposure", 'mort_tpm25_6cod_mean_total', 0, 150000, '0,0', 'MORT from total ' + u'PM\u2082.\u2085' + ' exposure (India = ' + '{:,}'.format(int(round(df.mort_tpm25_6cod_mean_total.values[-1], -3))) + ')'),
               ("MORT from ambient PM\u2082.\u2085 exposure", 'mort_apm25_6cod_mean_total', 0, 150000, '0,0', 'MORT from ambient ' + u'PM\u2082.\u2085' + ' exposure (India = ' + '{:,}'.format(int(round(df.mort_apm25_6cod_mean_total.values[-1], -3))) + ')'),
               ("MORT from household PM\u2082.\u2085 exposure", 'mort_hpm25_6cod_mean_total', 0, 150000, '0,0', 'MORT from household ' + u'PM\u2082.\u2085' + ' exposure (India = ' + '{:,}'.format(int(round(df.mort_hpm25_6cod_mean_total.values[-1], -3))) + ')'),
               ("DALYs rate from total PM\u2082.\u2085 exposure", 'dalys_tpm25_rate_6cod_mean_total', 0, 3500, '0,0', 'DALYs rate from total ' + u'PM\u2082.\u2085' + ' exposure (India = ' + '{:,}'.format(int(round(df.dalys_tpm25_rate_6cod_mean_total.values[-1]))) + ')'),
               ("DALYs rate from ambient PM\u2082.\u2085 exposure", 'dalys_apm25_rate_6cod_mean_total', 0, 3500, '0,0', 'DALYs rate from ambient ' + u'PM\u2082.\u2085' + ' exposure (India = ' + '{:,}'.format(int(round(df.dalys_apm25_rate_6cod_mean_total.values[-1]))) + ')'),
               ("DALYs rate from household PM\u2082.\u2085 exposure", 'dalys_hpm25_rate_6cod_mean_total', 0, 3500, '0,0', 'DALYs rate from household ' + u'PM\u2082.\u2085' + ' exposure (India = ' + '{:,}'.format(int(round(df.dalys_hpm25_rate_6cod_mean_total.values[-1]))) + ')'),
              ]
    format_df = pd.DataFrame(format_data, columns=['variable_map', 'variable' , 'min_range', 'max_range' , 'format', 'verbage'])
    format_df['scenario'] = scenario
    appended_format_df.append(format_df)

df_merged = pd.concat(appended_df, sort=False)
format_df_merged = pd.concat(appended_format_df, sort=False)

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Public health benefits of clean household energy in India"),
                        html.P(
                            """\
An interactive plot to visualise how various transitions to 
clean household energy in India impact air pollution and 
public health. For more information, see Conibear, L., 
et al. (2020). A complete transition to clean household energy 
can save one-quarter of the healthy life lost to particulate
matter pollution exposure in India. Environmental Research Letters."""
                        ),
                        html.H5("Scenario"),
                        html.Div(
                            [
                             dcc.Dropdown(
                                 id='scenario-select', value='BASELINE', searchable=False, clearable=False,
                                 options=[{'label':scenario, 'value':scenario} for scenario in scenarios],
                                 )
                             ]
                        ),
                        html.Ul(
                            [
                             html.Li('BASELINE = Present-day emissions.'),
                             html.Li('ALLLPG = Complete household transition from solid fuels to LPG.'),
                             html.Li('URB15 = Partial transition of ALLLPG within 15 km of urban areas.'),
                             html.Li('STATE50 = Emission reduction of URB15 applied evenly across each state.'),
                             html.Li('EMIS50 = Continued solid fuel use (stacking) at 50% after transitioning to LPG.')
                            ]
                        ),
                        html.H5("Variable"),
                        html.Div(
                            [
                             dcc.Dropdown(
                                 id='variable-select', value='apm25_popweighted', searchable=False, clearable=False,
                                 options=[{'label':row['variable_map'], 'value':row['variable']} for index, row in format_df.iterrows()],
                                 )
                            ]
                        ),
                        html.Ul(
                            [
                             html.Li('PM\u2082.\u2085 = Fine particulate matter.'),
                             html.Li('MORT = Premature mortality, per year.'),
                             html.Li('DALYs = Disability-adjusted life years, per year.')
                            ]
                        ),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        dcc.Graph(id='choropleth-graph'),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app.layout = html.Div([body])

@app.callback(
    dash.dependencies.Output('choropleth-graph', 'figure'),
        [
         dash.dependencies.Input('scenario-select', 'value'),
         dash.dependencies.Input('variable-select', 'value')
        ]
    )

def update_graph(scenario, variable):
    trace = go.Choroplethmapbox(z=df_merged[df_merged['scenario'] == scenario][variable],
                                locations=df_merged[df_merged['scenario'] == scenario]['geo-id'], geojson=geojsdata,
                                colorscale='YlOrRd', colorbar=dict(thickness=20, ticklen=3),
                                zmin=format_df[format_df['variable'] == variable]['min_range'].values[0],
                                zmax=format_df[format_df['variable'] == variable]['max_range'].values[0],
                                text=df_merged[df_merged['scenario'] == scenario]['location'],
                                marker_line_width=0.1, marker_opacity=0.7,
                                hovertemplate='<b>State</b>: <b>%{text}</b>'+ '<br> <b>Value </b>: %{z}<br>')
    layout = go.Layout(title=scenario + '<br>' + format_df_merged.loc[(format_df_merged['scenario'] == scenario) & (format_df_merged['variable'] == variable)]['verbage'].values[0], 
                       mapbox=dict(center=dict(lat=22.5, lon=83.0), accesstoken=mapboxt, zoom=3.8), margin=dict(t=100, b=0, l=0, r=0), height=700)
    return {'data':[trace], 'layout':layout}

if __name__ == '__main__':
    server.run(debug=True)
