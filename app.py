from utils.filter import filter_dataframe

import streamlit as st
import numpy as np, pandas as pd, time

#configuration of the page
st.set_page_config(layout = "wide")

#data loader
@st.cache_data 
def get_data():
     return pd.read_json('./data/result_tiger.json')[['出發地', '目的地', '日期', '星期', '金額', '往返']]

#display dataframes
try:
     st.image('./data/logo.png', width = 200)
except:
     st.image('https://static.tigerairtw.com/files/ttw-10th-logo-tc.png', width = 200)
st.title('Tigerair vizualisation tool')

#tab-page content
tab1, tab2, tab3 = st.tabs(["Ticket Information", "Optimal Trip", "About"])

with tab1:
     #load data
     with st.spinner('Preparing Data...'):
          time.sleep(2)
          df = filter_dataframe(get_data().replace([0], np.nan))
          df_go, df_back = df[df['往返']=='去程'][df.columns[:-1]], df[df['往返']=='回程'][df.columns[:-1]]
          df_back = df_back.rename({'出發地': '目的地', '目的地': '出發地'}, axis = 'columns')

     #dataframe
     st.subheader('去程機票')
     st.dataframe(df_go, use_container_width  = True, hide_index = True, height = 35 * 6 + 38)

     st.subheader('回程機票')
     st.dataframe(df_back, use_container_width  = True, hide_index = True, height = 35 * 6 +38)

with tab2:
     st.error('Still under development', icon="🚨")

with tab3:
     #about
     st.subheader("About")
     st.info(f"""
             This is an simple Webapp about TigerAir ticket information visualization!\n
             * You can find all data from [Tigerair API](https://api-book.tigerairtw.com/graphql)
             * And whole Webapp is developed via Streamlit Framework, check to their [offical pages](https://streamlit.io/gallery) for some inspirations 
             """)
     
     #todo list
     st.subheader("TODO List")
     st.checkbox("more detailed ticket information")
     st.checkbox("data pipeline from Ticket Data ETL to Streamlit Webapp")
     st.checkbox("optimal trip function")

#footer
footer="""<style>
.footer {
     position: fixed;
     left: 0;
     bottom: 0;
     width: 100%;
     color: rgb(5, 24, 85);
     text-align: center;
}
</style>
<div class="footer">
     <p>Copyright © 2024 All Rights Reserved by 
          <a href="https://github.com/xinhuang0716/TigerAir_with_Streamlit" target="_blank">
               XIN
          </a>.
     </p>
</div>
"""
st.markdown(footer, unsafe_allow_html = True)
