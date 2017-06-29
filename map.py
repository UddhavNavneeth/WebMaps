import folium
import pandas as pd
import numpy

data=pd.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elv=list(data["ELEV"])

def colorRange(elv):
	if elv<1000:
		return "green"
	elif 1000<=elv<=1500:
		return "blue"
	elif 1500<elv<=2000:
		return "orange"
	else:
		return "red"

m=folium.Map(location=[45,-90],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="Population")

for lt,ln,el in zip(lat,lon,elv):
	fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=7,popup=str(el)+"m",fill_color=colorRange(el),fill_opacity=0.7,color="grey"))

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),style_function=lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 10000000
else 'orange' if 10000000<= x["properties"]["POP2005"] <= 20000000 else 'red'}))

m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())

m.save("Webmap.html")
