import geopandas as gpd
import pandas as pd
import csv
from shapely.geometry import Point
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from address import Address

# Function to geocode an address if necessary
def geocode_address(Address):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(Address.get_street() + ", " + Address.get_city())
    if location:
        Address.update_lat(location.latitude)
        Address.update_long(location.longitude)
    return Address

if "__main__" == __name__:
    addresses = []
    file_path = "sf_trader_joes.csv"
    df = pd.read_csv(file_path)

    # Convert addresses to GeoDataFrame
    gdf = gpd.GeoDataFrame(df)
    print(gdf.head())

    # Define the point of interest (POI) or input address
    poi_address = "1458 Kansas St, San Francisco, CA"  # Example input address
    poi_location = Nominatim(user_agent="myGeocoder").geocode(poi_address)
    poi_point = Point(poi_location.longitude, poi_location.latitude)

    # Buffer around the POI to define the search radius (1 mile in this case)
    buffer_radius = 1  # in miles
    buffered_poi = poi_point.buffer(buffer_radius / 69.0)  # Convert miles to degrees

    # Filter addresses within the buffer radius
    addresses_within_radius = gdf[gdf.geometry.within(buffered_poi)]

    # Find the nearest address within the filtered addresses
    nearest_address = addresses_within_radius.distance(poi_point).idxmin()
    nearest_distance = addresses_within_radius.distance(poi_point).min()

    # Print the result
    if len(addresses_within_radius) > 0:
        print("Addresses within a {} mile radius of {}: ".format(buffer_radius, poi_address))
        print(addresses_within_radius)
        print("\nNearest address to {}: ".format(poi_address))
        print(addresses_within_radius.loc[nearest_address])
        print("Distance to nearest address: {:.2f} miles".format(nearest_distance))
    else:
        print("No addresses within a {} mile radius of {}.".format(buffer_radius, poi_address))
