import streamlit as st
import numpy as np, pandas as pd, os

#configuration of the page
st.set_page_config(layout = "wide")

#Loading the data
@st.cache_data 
def get_data():
     return pd.read_csv('./data/result_tiger.txt')[['出發地', '目的地', '日期', '星期', '金額', '往返']]

df = get_data().replace([0], np.nan)

df_go, df_back = df[df['往返']=='去程'][df.columns[:-1]], df[df['往返']=='回程'][df.columns[:-1]]
df_back = df_back.rename({'出發地': '目的地', '目的地': '出發地'}, axis = 'columns')

#display dataframes
st.write('test')
try:
     st.image('./data/logo.png', width = 200)
except:
     st.write('failed to load image')
st.title('Tigerair vizualisation tool')
st.markdown("""This app performs simple visualization from the airline data from TigerAir!""")

st.subheader('去程機票')
st.dataframe(df_go, use_container_width  = True, hide_index = True, height = 35 * 4 + 38)

st.subheader('回程機票')
st.dataframe(df_back, use_container_width  = True, hide_index = True, height = 35 * 4 +38)
