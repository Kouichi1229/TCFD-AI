import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# 自訂函式庫
import plt_data  
import ml_model
import load_data as ld


#App name
st.title('AI創新應用競賽-大台北TCFD')


# 欄位 : Data	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	
#        Month	RH-mean	TX-mean	WD-mean	RT-mean
# Loading data 
load='file_csv/'

all_df = pd.read_csv(load + '201302 to 2020_all2.csv')
sw_df = pd.read_csv(load + 'sw_data.csv')
bf_dt = pd.read_csv(load +'2014to2020gas.csv')
detail_df = pd.read_csv(load +'9908_10y_detail.csv')
df_PCR26 = pd.read_csv(load +'RCP2_6_year.csv')
df_PCR45 = pd.read_csv(load +'RCP4_5_year.csv')
df_PCR60 = pd.read_csv(load +'RCP6_0_year.csv')
df_PCR85 = pd.read_csv(load +'RCP8_5_year.csv')
df_gass1 = pd.read_csv(load +'gas_sheet_1.csv')

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
    st.subheader('取得原始資料')
    '#### 大台北產品營收 資料集(抓取過去瓦斯收入營收資料)'

    st.dataframe(detail_df)
    
    ''
    '#### 公用天然氣事業氣體售價表 資料集 '
    '###### ➜取得大台北過去單價資料'
    st.dataframe(df_gass1)
    ''
    st.subheader('將取得的資料作運算取得需要的欄位')
    st.markdown('$$\cfrac{瓦斯營收(月)}{單價(TWD/M^3)} = 月使用量(M^3)$$')
    ''
    st.subheader('測站月資料 臺北(466920)、天母(C0A9C0)、士林(C0A9E0)、信義(C0AC70)、松山(C0AH70)、平等(C0AH40)、社子(C0A980)')
    '##### 需要欄位 year(年) month(月) TX(平均溫度) RH(平均相對溼度) WD01(平均風速)'
    staNO_opt = st.selectbox('測站資料',('臺北 466920','天母 C0A9C0','士林 C0A9E0','信義 C0AC70','松山 C0AH70','平等 C0AH40','社子 C0A980'))
    if staNO_opt=='臺北 466920':
        ld.load_csv_file("466920")
    elif staNO_opt=='天母 C0A9C0':
        ld.load_csv_file("C0A9C0")
    elif staNO_opt=='士林 C0A9E0':
        ld.load_csv_file("C0A9E0")
    elif staNO_opt=='信義 C0AC70':
        ld.load_csv_file("C0AC70")
    elif staNO_opt=='松山 C0AH70':
        ld.load_csv_file("C0AH70")
    elif staNO_opt=='平等 C0AH40':
        ld.load_csv_file("C0AH40")
    else:
        ld.load_csv_file("C0A980")
    '#### 利用需要的欄位算出體感溫度'
    st.markdown('$$體感溫度(RT) = 1.04*T+0.2*e-0.65*V-2.7$$')
    st.markdown('$$e:\cfrac{RH}{100}*6.105*exp\cfrac{17.27*T}{237.7+T}(水氣壓 單位 hpa)$$')
    '###### ➣ T(氣溫 ℃)、e(水氣壓 hpa)、V(風速 m/sec)、RH(相對溼度 %)'
    '##### 將七站所有資料取平均值與營收資料做結合'
    ''
    st.subheader('2013/02~2020 大台北和測站資料 總整理')
    # 折線圖 營收與月份關係
    st.dataframe(all_df)
    ''
    ''
    st.subheader('資料圖視化')
    #歷年月份總使用量
    ''
    st.subheader('歷年月份與總使用量長條圖')
    month_option=st.selectbox('月份',
    ('1','2','3','4','5','6','7','8','9','10','11','12')
    )
    if month_option=='1':
        month=1
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='2':
        month=2
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='3':
        month=3
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='4':
        month=4
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='5':
        month=5
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='6':
        month=6
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='7':
        month=7
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='8':
        month=8
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='9':
        month=9
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='10':
        month=10
        plt_data.plt_Consumption_month_bar(month)
    elif month_option=='11':
        month=11
        plt_data.plt_Consumption_month_bar(month)
    else:
        month=12
        plt_data.plt_Consumption_month_bar(month)



    ''
    '#### 201302~2020 個月使用量'
    plt_data.print_everyyear_gas()
    '##### ➤ 很明顯的在 6 7 8 9 月(夏季) 瓦斯使用量偏低，在 12 1 2 3 月(冬季)時偏高'
    ''
    st.subheader('歷年與月平均溫度')
    month_v=st.slider("月份",1,12,6)
    plt_data.draw_tempure(month_v)
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
    v_tx = st.number_input('輸入想要推估的溫度(℃)')
    v_gas_tx = (-482543.05525943)*v_tx + 29876717.97914793
    vgstx_max = np.round((v_gas_tx+1191714.848))
    vgstx_min = np.round((v_gas_tx-1191714.848))
    st.markdown('#### 當月溫度為'+str(v_tx)+'℃時，推估月使用量為'+str(vgstx_min)+'~'+str(vgstx_max)+"(M^3)")
    ''
    '#### X:平均體感溫度 Y:使用量 算出體感溫度與使用量的最佳方程式'
    ml_model.RTmean_and_gas_ml()
    v_rt = st.number_input('輸入想要推估的體感溫度(℃)')
    v_gas_rt = (-365896.70973523)*v_tx + 27760988.330900572
    vgsrt_max= np.round((v_gas_rt+1201216.551))
    vgsrt_min= np.round((v_gas_rt-1201216.551))
    st.markdown('#### 當月體感溫度為'+str(v_rt)+'℃時，推估月使用量為'+str(vgsrt_min)+'~'+str(vgsrt_max)+"(M^3)")
    ''
    '#### 體感溫度/溫度 與 使用量 分佈圖疊合'
    ml_model.RtTx_and_gas_ml()



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