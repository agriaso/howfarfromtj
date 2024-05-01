class Address():
    def __init__(self, street, city, lat, long, inSanFrancisco):
        self.street = street
        self.city = city
        self.lat = float(lat)
        self.long = float(long)
        self.inSanFrancisco = inSanFrancisco

    def get_street(self):
        return self.street
    
    def get_city(self):
        return self.city
    
    def get_lat(self):
        return self.lat
    
    def get_long(self):
        return self.long
    
    def update_lat(self, lat):
        self.lat = lat

    def update_long(self, long):
        self.long = long

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.street, self.city, self.lat, self.long, self.inSanFrancisco)