'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import streamlit as st

import folium
import streamlit as st
from folium.features import DivIcon
from branca.element import Figure
from streamlit_folium import folium_static

# Set page outline and footer
st. set_page_config(layout="wide")

# Set the footer
footer="""<style>
a:link , a:visited{
color: #D891FC;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a href="https://www.github.com/mbidinlib/" target="_blank">Mathew Bidinlib </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


#Header
st.markdown("""<center><b><h3><font color = 'maroon'>MGlory Data Visualization</font></h3></b>
    </center>""",unsafe_allow_html=True)



with st.sidebar:
# Define the sidebar
    st.markdown("""<b>Welcome to <a href="https://www.github.com/mbidinlib/" target="_blank">MGlory </a> Data Visualization toolkit. 
    This tool will help you visualize your data in charts, maps and others</b>""",unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown("<h5><u>Data Selection</u></h5>",unsafe_allow_html=True)
    with  st.expander("Click here to import data",expanded=False):
        ds = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
        if ds:
            st.session_state["ds"] = ds


    st.markdown("## Display Mode")
    display = st.radio("",('Dataset', 'Chart'))
    st.image('picture.jpg',
        width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.markdown('<a href="https://www.github.com/mbidinlib/" target="_blank">Mathew Bidinlib </a>',unsafe_allow_html=True)

hcol1, hcol2,hcol3 = st.columns((2,0.4,4))

with hcol1:
    st.markdown("")
    st.markdown("")
    option = st.selectbox(
        'Select visualization type',
        ('Bar','Goegraphic'))

with hcol2:
    ""
    

with hcol3:
    # Read data
    if "ds" in st.session_state:
        df= st.session_state["ds"]
        file_ext = df.name.split('.')[-1]  # get file extension of selected file

        if file_ext == 'csv':
            dataset = pd.read_csv(df)
            #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove  
            st.session_state["dataset"] = dataset                         
        elif file_ext == 'xls'or file_ext == 'xlsx':
            dataset = pd.read_excel(df, engine='openpyxl').astype(str)
            st.session_state["dataset"] = dataset
            #st.dataframe(pd.read_excel(df1))
        else:
            st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
            #Support for Other file extensions would be added later**""")
        
        
        
        
        # Define plots
        ##############
        #Maps
        loc = "Plot of Coordinates"
        title_html = '''
        <h1 style="text-align: center; font-size: 18px; font-weight: bold; color: 
            #ffffff; background-color: #e02b20; padding: 10px 0px;margin:0px">{}</h1>
        '''.format(loc)

        data =  dataset
        lat = data.lat
        lon = data.lon
        name = data.name 

        fig2=Figure(width=550,height=350)
        m = folium.Map(location=[(lat.max()+ lat.min())/2,
                                (lon.max()+ lon.min())/2], zoom_start=5)
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


            
            
            
            
        if display == "Dataset":
            st.markdown("<h5><u>Data Overview</u></h5>",unsafe_allow_html=True)
            st.dataframe(dataset)
        elif display =="Chart":
            st.markdown("<h5><u>Charts</u></h5>",unsafe_allow_html=True)
            folium_static(m)

            





