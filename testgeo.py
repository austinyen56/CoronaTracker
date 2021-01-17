import geocoder
g = geocoder.ip('Me')
print("Your location:",g.latlng)