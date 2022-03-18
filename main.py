import folium
import pandas
from folium import Map


# getting volcanoes data
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


# colors for volcanoes markers based on elevation
def color_maker(elevation):
    if elevation < 1000:
        return "Green"
    elif 1000 <= elevation < 3000:
        return "Orange"
    else:
        return "Red"


# centring map on start
map: Map = folium.Map(location=[39.10, -94.57], zoom_start=4, titles="openstreetmap")

# adding markers for volcanoes
fg = folium.FeatureGroup(name='Volcanoes markers')
for lt, lo, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=(lt, lo), radius=6, popup=str(el) + " m",
                                     fill_color=color_maker(el), color="Grey", fill_opacity=0.8))

# adding color tiles for countries based on population and hovering over shows name and population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                             style_function=lambda x: {"fillColor": "Green" if x["properties"]["POP2005"] < 10000000
                             else "Red"}, tooltip=folium.GeoJsonTooltip(fields=('NAME', 'POP2005',))))


map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
