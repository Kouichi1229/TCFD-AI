import pandas as pd
import streamlit as st


load='file_csv/'
all_df = pd.read_csv(load + '201302 to 2020_all2.csv')


def load_csv_file(fileN):
    df = pd.read_csv(load+str(fileN)+'.csv')
    st.dataframe(df)


# 欄位 : Data	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	
#        Month	RH-mean	TX-mean	WD-mean	AT-mean Consumption for one of family(m^3)
def print_data_corr():
    df=all_df
    corr_data_set = ['Consumption(m^3)','RH-mean','TX-mean','WD-mean','AT-mean']
    data_corr = df[corr_data_set].corr()
    corr_res=pd.DataFrame(data_corr['Consumption(m^3)'])
    st.dataframe(corr_res)
