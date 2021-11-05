import pandas as pd
import streamlit as st

load='file_csv/'


def load_csv_file(fileN):
    df = pd.read_csv(load+str(fileN)+'.csv')
    st.dataframe(df)
