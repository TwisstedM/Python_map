import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_maker(elevation):
    if elevation < 1000:
        return "Green"
    elif 1000 <= elevation < 3000:
        return "Orange"
    else:
        return "Red"


map = folium.Map(location=[39.10, -94.57], zoom_start=6, titles="Stamen Terrain")


fg = folium.FeatureGroup(name='Test map')
for lt, lo, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=(lt, lo), radius=6, popup=str(el)+" m",
                                     fill_color=color_maker(el), color="Grey", fill_opacity=0.8))


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig"),
                             style_function=lambda x: {"fillColor": "Green" if x["properties"]["POP2005"] < 10000000
                             else "Red"}))


map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
