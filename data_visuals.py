'''
Date: Wed Aug 23 21:12:18 2022
@author: Glooory
Purpose: Data Engineering
'''
from io import StringIO
import pandas as pd
import streamlit as st

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
    st.markdown("""Welcome to MGlory Data Visualization toolkit. 
    This tool will help you visualize your data in charts, maps and others""")
    st.markdown("")
    st.markdown("")

    st.markdown("# Options")
    display = st.radio(
    "Display",
    ('Dataset', 'Chart'))
    st.image('picture.jpg',
        width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown('<a href="https://www.github.com/mbidinlib/" target="_blank">Mathew Bidinlib </a>',unsafe_allow_html=True)

hcol1, hcol2,hcol3 = st.columns((2,0.4,4))

with hcol1:
    st.markdown("")
    st.markdown("<h5><u>Data Selection</u></h5>",unsafe_allow_html=True)
    ds = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
    if ds:
        st.session_state["ds"] = ds

    st.markdown("")
    st.markdown("")

with hcol2:
    ""

with hcol3:
    # Read data
    if "ds" in st.session_state:
        df= st.session_state["ds"]
        file_ext = df.name.split('.')[-1]  # get file extension of selected file

        if file_ext == 'csv':
            dataset_1 = pd.read_csv(df)
            #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove  
            st.session_state["dataset1"] = dataset_1                         
        elif file_ext == 'xls'or file_ext == 'xlsx':
            dataset_1 = pd.read_excel(df, engine='openpyxl').astype(str)
            st.session_state["dataset1"] = dataset_1
            #st.dataframe(pd.read_excel(df1))
        else:
            st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
            #Support for Other file extensions would be added later**""")
        if display == "Dataset":
            st.header("Data overview")  # Give it a header
            st.dataframe(dataset_1)
        elif display =="Chart":
            st.header("Chart overview")  # Give it a header






