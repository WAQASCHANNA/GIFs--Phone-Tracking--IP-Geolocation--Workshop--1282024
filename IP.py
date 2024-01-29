import geocoder
import folium
from decimal import Decimal
#IP
g= geocoder.ip("103.82.121.24")
myAddress= g.latlng
print(myAddress)
#Map
my_map = folium.Map(location=myAddress, zoom_start=12)
folium.CircleMarker (location=myAddress, radius=50, popup= "WAQAS").add_to(my_map)
folium.Marker(myAddress,popup="WAQAS").add_to(my_map)
my_map.save("my_map.html")
