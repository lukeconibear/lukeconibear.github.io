import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString, MultiLineString
import numpy as np

def shapefile_to_geojson(gdf, index_list, level=1, tolerance=0.025):
    """
    Description:
        Converts shapefile to geojson that can be used as a plotly go.Choroplethmapbox.
    Args:    
        gdf (str): Path to geojson shapefile.
        index_list (list): Sublist of list(gdf.index) or gdf.index for all data.
        level (int, default=1): Shapefile level, 0=country, 1=state/province, 2=city/prefecture, etc.
        tolerance (float, default=0.025): Parameter to set the Polygon/MultiPolygon degree of simplification.
    Returns:
        geojson (dict): Dictionary of converted json shapefile.
    """
    geo_names = list(gdf[f'NAME_{level}'])
    geojson = {'type':'FeatureCollection', 'features':[]}
    for index in index_list:
        geo = gdf['geometry'][index].simplify(tolerance)
        if isinstance(geo.boundary, LineString):
            gtype = 'Polygon'
            bcoords = np.dstack(geo.boundary.coords.xy).tolist()
        elif isinstance(geo.boundary, MultiLineString):
            gtype = 'MultiPolygon'
            bcoords = []
            for b in geo.boundary:
                x, y = b.coords.xy
                coords = np.dstack((x,y)).tolist()
                bcoords.append(coords)
        else: pass
        feature = {'type':'Feature',
                   'id':index,
                   'properties':{'name':geo_names[index]},
                   'geometry':{'type':gtype, 'coordinates': bcoords},
                   }
        geojson['features'].append(feature)
    return geojson
