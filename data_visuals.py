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




# Define the sidebar
st.sidebar.markdown("#Options")
with st.sidebar.container():
   sbcol1, sbcol2, = st.columns(2)

   sbcol1.image('picture.jpg',
        caption='Mathew Bidinlib', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("""<b><h3><font color = 'maroon'>MGlory Data Visualization</font></h3></b>
    Welcome to MGlory Data Visualization toolkit.
    This tool will help you visualize your data in charts, maps and other
    """,unsafe_allow_html=True)

hcol1, hcol2 = st.columns(2)

with hcol1:
    st.markdown("<h4><u>Import Page</u></h4>",unsafe_allow_html=True)
    exp1 = st.expander("Help note",expanded=False)
    st.subheader("Select file")
    ds = st.file_uploader("Select Data file", type=["csv", 'xlsx'], key = "data1")
    if ds:
        st.session_state["ds"] = ds

    st.markdown("")
    st.markdown("")


with hcol2:
    # Read data
    if "ds" in st.session_state:
        st.header("Data and Chart overview")  # Give it a header
        df= st.session_state["ds1"]
        file_ext = df.name.split('.')[-1]  # get file extension of selected file

        if file_ext == 'csv':
            dataset_1 = pd.read_csv(df)
            st.dataframe(dataset_1) 
            #st.dataframe(pd.read_csv(StringIO(df1),dtype='unicode')) ### Remove  
            st.session_state["dataset1"] = dataset_1                         
        elif file_ext == 'xls'or file_ext == 'xlsx':
            dataset_1 = pd.read_excel(df, engine='openpyxl').astype(str)
            st.dataframe(dataset_1)
            st.session_state["dataset1"] = dataset_1
            #st.dataframe(pd.read_excel(df1))
        else:
            st.markdown("""**This file is type is currently not accepted. Upload a file with a .csv or xls extenssion. 
            #Support for Other file extensions would be added later**""")




