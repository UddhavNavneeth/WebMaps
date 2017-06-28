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
fg=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elv):
	fg.add_child(folium.CircleMarker(location=[lt,ln],radius=7,popup=str(el)+"m",fill_color=colorRange(el),fill_opacity=0.7,color="grey"))
m.add_child(fg)


m.save("Random1.html")
