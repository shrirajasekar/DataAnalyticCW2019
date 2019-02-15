import folium
import os
m = folium.Map(location=[42.6300, -71.8888], zoom_control=12)
#Generates a MAP
#Create a marker
tooltip = 'Click here for information'
folium.Marker([42.6300, -71.8888], 
                    popup='<strong>Location 1</strong>',
                    tooltip=tooltip).add_to(m)
m.save('map.html') 
