from measure_distance import load_trader_joe_data, geocode, is_in_range

data_path = "sf_trader_joes.csv"

def test_load_trader_joe_data():
    trader_joe_gdf = load_trader_joe_data(data_path)
    assert trader_joe_gdf is not None

def test_geocode():
    location = geocode("photon", dict(), "1458 Kansas St, San Francisco, CA")
    assert location is not None

def test_is_in_range():
    gdf = load_trader_joe_data(data_path)
    addresses_in_range = is_in_range(gdf, geocode("photon", dict(), "1458 Kansas Street, San Francisco"), 2)
    assert addresses_in_range is not None
    assert len(addresses_in_range) == 1