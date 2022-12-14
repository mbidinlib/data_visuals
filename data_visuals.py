'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import folium
import streamlit as st
from folium.features import DivIcon
from branca.element import Figure
from streamlit_folium import folium_static
import seaborn as sns

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
st.markdown(""" ## <center><b><h3><font color = 'maroon'>MGlory Data Visualization</font></h3></b>
    </center>""",unsafe_allow_html=True)

with st.sidebar:
# Define the sidebar

    st.markdown(""" ## <b>Welcome to <a href="https://www.github.com/mbidinlib/" target="_blank">MGlory </a> Data Visualization toolkit. This is a python based toolkit that helps you visualize your data</b>""",unsafe_allow_html=True)
    st.markdown("")

    st.markdown( """# <u>Get Started</u>""", unsafe_allow_html=True)
    
    st.markdown("## Data Selection",unsafe_allow_html=True)
    with  st.expander("Click here to import data",expanded=False):
        ds = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
        if ds:
            st.session_state["ds"] = ds
                # Read data

    st.markdown("## Display Mode")
    display = st.radio("",('Dataset', 'Chart'))
    st.image('picture.jpg',
        width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.markdown('<a href="https://www.github.com/mbidinlib/" target="_blank">Mathew Bidinlib </a>',unsafe_allow_html=True)

hcol1, hcol2, hcol3 = st.columns((1,4,0.2))
if not("ds" in st.session_state):
    st.markdown("## Select Dataset at the sidebar")
with hcol1:
    st.markdown("")
    st.markdown("")
    if "ds" in st.session_state:
        
        # Import Data
        df= st.session_state["ds"]
        file_ext = df.name.split('.')[-1]  # get file extension of selected file

        # CSV file
        if file_ext == 'csv':
            dataset = pd.read_csv(df)
            #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove  
            st.session_state["dataset"] = dataset 
        #Excel file
        elif file_ext == 'xls'or file_ext == 'xlsx':
            dataset = pd.read_excel(df, engine='openpyxl').astype(str)
            st.session_state["dataset"] = dataset
            #st.dataframe(pd.read_excel(df1))
        else:
            st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
            #Support for Other file extensions would be added later**""")
    
        dataset.insert(0,"","")
        columns = dataset.columns
        type = st.selectbox(
            'Select visualization type',
            ('Line', 'Bar','Scatter','Goespatial'))

        # Define Scatter inputs
        if type == 'Scatter':
            # Main variables
            with  st.expander("Main variable selection",expanded=False):
                xvar = st.selectbox(
                    'Select x variable',
                    columns)    
                yvar = st.selectbox(
                    'Select y variable',
                    columns)
            # Additional parameters
            if  xvar !=""  or yvar !="":
                with  st.expander("Additional parameters",expanded=False):
                    stitle = st.text_input("Y label", "Scatter plot")
                    sxlab = st.text_input("X label", "X-axis")
                    sylab = st.text_input("Y label", "Y-axis")
                    #Plot color
                    scolor = st.color_picker('Plot color', '#0A8FBF', key="scolor")
                    # Gridlines
                    sshowgrid = st.selectbox('show gid lines', ('No', 'Yes'))
                    if sshowgrid =='Yes':
                        sgridcolor = st.color_picker('Grid color', '#0A8FBF', key="scolor")
                        sgridaxis = st.selectbox('Grid axis', ('both','x', 'y'))



        # Define Line inputs
        if type == 'Line':
            # Main variables
            with  st.expander("Variable selection",expanded=False):
                    linevars = st.multiselect("""Select the variables for the line plot. 
                                              """, columns)
            if  linevars  !="" :
                with  st.expander("Additional parameters",expanded=False):
                    lxlab = st.text_input("X label", "X-axis")
                    lylab = st.text_input("Y label", "Y-axis")
                    lineloc = st.selectbox('Location of legend',
                        ('best', 'upper right', 'upper left','lower left', 
                         'lower right', 'right', 'center left', 'center right',
                         'lower center', 'upper center','center'))    
                    lshowleg = st.selectbox('Show legend', ("Yes", "No"))
                    if lshowleg == "Yes":
                        llegshad = st.selectbox('Legend Shadow', ("False", "True"))
                        llegsize = st.selectbox("Legend size", 
                                               ('xx-small', 'x-small', 'small', 'medium', 
                                                'large', 'x-large', 'xx-large'),
                                                )
                    lshowgrid = st.selectbox('show gid lines', ('No', 'Yes'))
                    if lshowgrid =='Yes':
                        lgridcolor = st.color_picker('Grid color', '#0A8FBF', key="scolor")
                        lgridaxis = st.selectbox('Grid axis', ('both','x', 'y'))

        # Define bar inputs
        if type == 'Bar':
            # Main variables
            with  st.expander("Variable selection. For horizontal bars, the X should be the values",expanded=False):
                    bxvars = st.selectbox("""Select X Variable 
                                              """, columns)
                    byvars = st.selectbox("""Select the y variable 
                                              """, columns)

            if  bxvars  !="" and bxvars != "" :
                with  st.expander("Additional parameters",expanded=False):
                    bxlab = st.text_input("X label", bxvars)
                    bylab = st.text_input("Y label", byvars)
                    berrorb = st.selectbox('show error bars', ('No', 'Yes'))
                    if berrorb =='Yes':
                        berrorci = st.number_input('Confidence Interval of error', 5,99)
                    
                    #bgridaxis = st.selectbox('Grid axis', ('both','x', 'y'))
                
                    
                    
                    # Gridline options
                    #bshowgrid = st.selectbox('show gid bars', ('No', 'Yes'))
                    
                    #if bshowgrid =='Yes':
                    #    bgridcolor = st.color_picker('Grid color', '#0A8FBF', key="scolor")
                    #    bgridaxis = st.selectbox('Grid axis', ('both','x', 'y'))
                    # Bar legend for group bars
                    bshowleg = st.selectbox('Group/Show legend', ("Yes", "No"))
                    if bshowleg == "Yes":
                        blegvar = st.selectbox('Group/Legend variable', columns)

#                        blegsize = st.selectbox("Legend size", 
#                                               ('xx-small', 'x-small', 'small', 'medium', 
#                                                'large', 'x-large', 'xx-large'),
#                                               )

     
        
        # Define geospatial inputs
        if type == 'Goespatial':
            with  st.expander("Main variable selection",expanded=False):
                lonvar = st.selectbox(
                    'Select Longitude variable',
                    columns)    
                latvar = st.selectbox(
                    'Select Latitude variable',
                    columns)    
            with  st.expander("Additional parameters",expanded=False):
                namevar = st.selectbox(
                            'Select Label variable',
                            columns)
with hcol2:       
    
    # Trigger display
    if "dataset" in st.session_state and display == "Dataset":
        st.markdown("<h5><u>Data Overview</u></h5>",unsafe_allow_html=True)
        st.dataframe(dataset)
        
    if "dataset" in st.session_state and display == "Chart":   
        
        #############
        # Define plots
        ##############
        
        #Scatter plot
        if type == 'Scatter' and xvar !="" and yvar !="":
            fig, scatter = plt.subplots()
            scatter= plt.scatter(dataset[xvar], dataset[yvar], c= scolor)
            plt.xlabel(sxlab)
            plt.ylabel(sylab)
            if sshowgrid =='Yes':
                plt.grid(color=sgridcolor, axis = sgridaxis)
            st.pyplot(fig)

        # Line Plot
        if type == 'Line' and linevars !="":
            fig, line = plt.subplots()
            for j in linevars:
                line= plt.plot(dataset[j], label=j)
            if lshowleg == 'Yes':
                plt.legend(loc=lineloc, shadow=llegshad, fontsize=llegsize)
            plt.xlabel(lxlab)
            plt.ylabel(lylab)
            if lshowgrid =='Yes':
                plt.grid(color=lgridcolor, axis = lgridaxis)
            st.pyplot(fig)
            
            
        # bar Plot
        if type == 'Bar' and bxvars !="" and byvars !="":

            if berrorb =='Yes':
                bci = berrorci
            else: bci = None
                
            if bshowleg == "Yes":
                hueval = blegvar
            else : hueval = bxvars
                
                
            fig = plt.figure(figsize=(10, 8))
            bar= sns.barplot(data = dataset, x= bxvars, y= byvars, 
                             ci=bci, hue=hueval)
            bar.set(xlabel=bxlab, ylabel=bylab)
 
      #       if bshowleg == 'Yes':
     #           plt.legend(loc=barloc, shadow=blegshad, fontsize=blegsize)
    #        plt.xlabel(bxlab)
   #         plt.ylabel(bylab)
  #          if bshowgrid =='Yes':
 #               plt.grid(color=bgridcolor, axis = bgridaxis)
#
            st.pyplot(fig)
            
            

        #Geographic Plots
        if type == 'Goespatial' and lonvar !="" and latvar !="":
            loc = "Plot of Coordinates"
            title_html = '''
            <h1 style="text-align: center; font-size: 18px; font-weight: bold; color: 
                #ffffff; background-color: #e02b20; padding: 10px 0px;margin:0px">{}</h1>
            '''.format(loc)

            data =  dataset
            lat = dataset[latvar]
            lon = dataset[lonvar]
            name = data[namevar] 

            # Draw initial map
            fig2=Figure(width=310,height=310)
            m = folium.Map(location=[(lat.max()+ lat.min())/2,
                                    (lon.max()+ lon.min())/2], zoom_start=6)
            
            #Add markers
            for i in range(0,len(data)):
                folium.Marker(
                    location=[data.iloc[i][latvar], data.iloc[i][lonvar]],
                    popup=data.iloc[i][namevar],
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
            
            #Add Layers and tiles
            folium.TileLayer('Stamen Terrain').add_to(m)
            folium.TileLayer('Stamen Toner').add_to(m)
            folium.TileLayer('Stamen Water Color').add_to(m)
            folium.TileLayer('cartodbpositron').add_to(m)
            folium.TileLayer('cartodbdark_matter').add_to(m)
            
            #Layers
            fig2.add_child(m)
            folium.LayerControl().add_to(m)
            #Add title
            m.get_root().html.add_child(folium.Element(title_html))   
                    
                    
            # Show Charts
            #Geographic Plots
            st.markdown(f"""<h5><u>Geospatial Plot of {lonvar} and {latvar} variables</u></h5>""",unsafe_allow_html=True)
            folium_static(m)



with hcol3:
    st.markdown("")

