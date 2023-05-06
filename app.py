
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Recession Indicator',
                  page_icon=":bar_chart:",
                  layout='wide'
                  )

ultimate_df = pd.read_excel(
                io='ultimate_workbook.xlsx',
                engine='openpyxl',
                sheet_name = 'Sheet1',
                usecols='B:F',
                nrows=601
                )

#Sidebar settings:
st.sidebar.header('Please Filter here based on the Year and the Quarter desired:')

year = st.sidebar.slider(
    "Select the range for years:",
    min_value=1973.0,
    max_value=2022.0,
    value=(1990.0,2022.0),
    step=0.25
)

quarter = st.sidebar.multiselect(
        "Select the quarter here:",
    options=ultimate_df['QUARTER'].unique(),
    default=1)

df_selection = ultimate_df.query(
    'YEAR >= @year[0] and YEAR <= @year[1] and QUARTER == @quarter')


# --- Header ---
st.title(":bar_chart: Recession Indicators")

# ---Side text for Recession History---
with st.expander('', expanded=True):
    r_col, m_col, l_col = st.columns(3)
    
    with r_col:
        st.markdown(f'''
        #### What is recession?
        A recession is most often defined as an economic contraction of atleast 2% of the prior GDP for two consecutive quarters. Among many other indicators, a blow-up in credit volume followed by an increase in consumer prices are considered to be the messengers of a pending recession.
        ''', unsafe_allow_html=True)
    
    with m_col:
        st.markdown(f'''
        #### Indicators outlined in the project:
        <ul>
            <li><strong>A decline in GDP:</strong> A decline in GDP of more than 2% over two consecutive quarters.</li>
            <li><strong>Increase in Credit Volume:</strong> Given that recession follows a peak in the market economy when consumers are spending extensively based on credit under the pretense that everything is alright.
            <li><strong>Increase in Consumer Prices:</strong> Given that people are spending more which increases demand, which in turn increases the prices of things.
            ''', unsafe_allow_html=True)
    
    with l_col:
        st.markdown(f'''
        #### A Brief list of all the Recessions to hit US since The Great Depression:
        <ol style="padding-left:20px">
          <li>May 1937-June 1938</li>
          <li>February 1995-October 1995</li>
          <li>November 1948-October-1949</li>
          <li>July 1953-May 1954</li>
          <li>August 1957-April 1958</li>
          <li>April 1960-February 1961</li>
          <li>December 1969-November 1970</li>
          <li>November 1973-March 1975</li>
          <li>January 1980-July 1980</li>
          <li>July 1981-November 1982</li>
          <li>July 1990-March 1991</li>
          <li>March 2001-November 2001</li>
          <li>December 2007-June 2009</li>
          <li>February 2020-June 2020</li>
        </ol>
        
        ''', unsafe_allow_html=True)
