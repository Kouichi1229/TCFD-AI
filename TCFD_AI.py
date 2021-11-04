import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# 自訂函式庫
import plt_data  
import ml_model

#App name
st.title('AI創新應用競賽-大台北TCFD')


# 欄位 : Data	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	
#        Month	RH-mean	TX-mean	WD-mean	RT-mean
# Loading data 
load='file_csv/'
all_df = pd.read_csv(load + '201302 to 2020_all2.csv')
sw_df = pd.read_csv(load + 'sw_data.csv')
bf_dt = pd.read_csv(load +'2014to2020gas.csv')
df_PCR26 = pd.read_csv(load +'RCP2_6_year.csv')
df_PCR45 = pd.read_csv(load +'RCP4_5_year.csv')
df_PCR60 = pd.read_csv(load +'RCP6_0_year.csv')
df_PCR85 = pd.read_csv(load +'RCP8_5_year.csv')
# Show first data 
''



#選單
sidebar = st.sidebar.selectbox(
    "快速選單",
    ("大台北簡介", "資料集和資料視覺化", "機器學習","未來影響")
)

if sidebar=='大台北簡介':
    st.subheader('大台北業務項目 201112~202109 平均比例')
    plt_data.piechart()
    #選擇測站資料
    ''
    '#### 大台北主要服務地區分佈在：' 
    '##### 松山、信義、大安、大同、萬華、中正、中山、士林'
    st.image('pic/測站位置圖.png', caption='StNO postion')
    '##### 選擇台北、天母、士林、信義、松山、平等、社子共７個測站的平均資料做分析'
    ''
elif sidebar=='資料集和資料視覺化':
    st.subheader('2013/02~2020 大台北和測站資料')
    # 折線圖 營收與月份關係
    st.dataframe(all_df)
    ''
    st.subheader('資料圖視化')
    ''
    '#### 201302~2020 個月使用量'
    plt_data.print_everyyear_gas()
    '##### ➤ 很明顯的在 6 7 8 9 月(夏季) 瓦斯使用量偏低，在 12 1 2 3 月(冬季)時偏高'

    ''
    '#### 溫度與使用量分布圖'
    plt_data.print_TXmean_and_gas()
    '##### ➤當溫度越高時，使用量明顯變低'

    ''
    '#### 體感溫度與使用量分布圖'
    plt_data.print_RTmean_and_gas()
    ''

    '#### 體感溫度&溫度疊合'
    plt_data.print_RTmeantoTXmean()

elif sidebar=='機器學習':
    st.subheader("機器學習 線性回歸(Linear Resgression)")
    '#### X:平均溫度 Y:使用量 算出溫度與使用量的最佳方程式'
    ml_model.TXmean_and_gas_ml()
    '#### X:平均體感溫度 Y:使用量 算出體感溫度與使用量的最佳方程式'
    ml_model.RTmean_and_gas_ml()
    '#### 體感溫度/溫度 與 使用量 分佈圖疊合'
    #RtTx_and_gas_ml()



elif sidebar=='未來影響':
    st.subheader('在RCP各情境的影響下')
    selectbox_RCP = st.selectbox(
    "RCP",
    ("None", "RCP2.6", "RCP4.5","RCP6.0",'RCP8.5'))
    if selectbox_RCP=='None':
        st.subheader('總覽')
        #st.image('pic/ALL RCP figure.png', caption='ALL RCP figure')
        plt_data.draw_all_pcr()
    elif selectbox_RCP=='RCP2.6':
        dfload=df_PCR26
        N="RCP2.6"
        plt_data.draw_pcr(dfload,N)
    elif selectbox_RCP=='RCP4.5':
        dfload=df_PCR45
        N="RCP4.5"
        plt_data.draw_pcr(dfload,N)
    elif selectbox_RCP=='RCP6.0':
        dfload=df_PCR60
        N="RCP6.0"
        plt_data.draw_pcr(dfload,N)
    else :
        dfload=df_PCR85
        N="RCP8.5"
        plt_data.draw_pcr(dfload,N)