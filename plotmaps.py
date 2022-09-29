# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import folium
import pandas as pd
import streamlit as st
from folium.features import DivIcon
from branca.element import Figure

import data_visuals as idata

# Step 1
loc = "Plot of Coordinates"
title_html = '''
<h1 style="text-align: center; font-size: 18px; font-weight: bold; color: 
    #ffffff; background-color: #e02b20; padding: 10px 0px;margin:0px">{}</h1>
'''.format(loc)

data =  pd.read_csv("C:/Users/STAFF/Documents/GitHub/data")

#Step 4
lat = data.lat
lon = data.lon
name = data.name 

fig2=Figure(width=550,height=350)
m = folium.Map(location=[(lat.max()+ lat.min())/2,
                         (lon.max()+ lon.min())/2], zoom_start=5)




# Step 4

for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
      icon=folium.Icon(color = 'black', icon='info-sign')
   ).add_to(m)



# Add custom base maps to folium
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = False,
        control = False
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}



# Add custom basemaps
basemaps['Google Maps'].add_to(m)
basemaps['Google Satellite Hybrid'].add_to(m)

#Layers
fig2.add_child(m)
folium.LayerControl().add_to(m)

#Add title
m.get_root().html.add_child(folium.Element(title_html))
   
#m.save('index.html')
#m.save('index.png') 
    
    
    
    

    
    
    
    