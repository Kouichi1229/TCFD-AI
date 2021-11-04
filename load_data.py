import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np




@st.cache
def load_data():
	df=pd.read_excel('file_csv/all_gas_c_oneprice.xlsx')
	return df