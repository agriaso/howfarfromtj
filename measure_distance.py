import geopandas as gpd
import pandas as pd
import csv
from shapely.geometry import Point
from geopy.distance import geodesic
from geopy.geocoders import get_geocoder_for_service

def load_trader_joe_data(file_path):
    trader_joe_data = pd.read_csv(file_path)
    trader_joe_data['geometry'] = trader_joe_data.apply(lambda x: Point((float(x['Long']), float(x['Lat']))), axis=1)
    trader_joe_gdf = gpd.GeoDataFrame(trader_joe_data, geometry='geometry')
    return trader_joe_gdf

def geocode(geocoder, config, query):
    cls = get_geocoder_for_service(geocoder)
    geolocator = cls(**config)
    location = geolocator.geocode(query)
    return location

def is_in_range(gdf, poi_location, buffer_radius):
    poi_point = Point(poi_location.longitude, poi_location.latitude)
    buffered_poi = poi_point.buffer(buffer_radius / 69.0)
    addresses_in_range = gdf[gdf.geometry.within(buffered_poi)]
    return addresses_in_range



