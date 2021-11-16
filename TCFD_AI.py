import streamlit as st
import pandas as pd 
import numpy as np


# 自訂函式庫
import plt_data  
import ml_model
import load_data as ld
import txt
#App name
st.title('AI創新應用競賽-大台北TCFD')


# 欄位 : Date	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	
#        Month	RH-mean	TX-mean	WD-mean	AT-mean Consumption for one of family(m^3)
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
df_subscriber = pd.read_csv(load +'subscriber_number.csv')
df_pPCR26 =pd.read_csv(load +'RCP2_6predict.csv')
df_pPCR45 =pd.read_csv(load +'RCP4_5predict.csv')
df_pPCR60 =pd.read_csv(load +'RCP6_0predict.csv')
df_pPCR85 =pd.read_csv(load +'RCP8_5predict.csv')
df_C_standard = pd.read_csv(load+'standard_Consumption .csv')



''


#選單
sidebar = st.sidebar.selectbox(
    "快速選單",
    ("大台北簡介", "資料集和資料視覺化", "機器學習","未來影響")
)

if sidebar=='大台北簡介':
    #txt.print_movition()
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
    st.markdown('$$\cfrac{瓦斯月營收(TWD)}{月單價(TWD/M^3)} = 月總使用量(M^3)$$')
    ''
    st.subheader('大台北每年用戶人數')
    st.dataframe(df_subscriber)
    st.markdown('$$\cfrac{月總使用量(M^3)}{用戶人數} = 每戶月使用量(M^3)$$')
    ''
    st.subheader('測站月資料 臺北(466920)、天母(C0A9C0)、士林(C0A9E0)、信義(C0AC70)、松山(C0AH70)、平等(C0AH40)、社子(C0A980)')
    '##### 需要欄位 year(年) month(月) TX(平均溫度) RH(平均相對溼度) WD01(平均風速)'
    ''
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
    st.markdown('$$體感溫度(AT) = 1.04*T+0.2*e-0.65*V-2.7$$')
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
    st.subheader('歷年月份與使用量長條圖')
    rbt_consumption = st.radio(
    '長條圖顯示',('總累積使用量','單戶使用量')
    )
    month_option=st.selectbox('月份',
    ('1','2','3','4','5','6','7','8','9','10','11','12')
    )
    if month_option=='1':
        month=1
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='2':
        month=2
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='3':
        month=3
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='4':
        month=4
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='5':
        month=5
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='6':
        month=6
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='7':
        month=7
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='8':
        month=8
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='9':
        month=9
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='10':
        month=10
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    elif month_option=='11':
        month=11
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)
    else:
        month=12
        if rbt_consumption =='總累積使用量':
            plt_data.plt_Consumption_month_bar(month)
        else:
            plt_data.plt_oneoffamily_month_bar(month)

    ''
    select_plot_consumption = st.radio(
     "選擇想視覺化的參數",
     ('各月總使用量', '各月單用戶使用量'))

    if select_plot_consumption == '各月總使用量':
        '#### 201302~2020 各月使用量'
        plt_data.print_everyyear_gas()
        ''
        year_option = st.selectbox('年',
        ('2013','2014','2015','2016','2017','2018','2019','2020')
        )
        if year_option=='2013':
            year ='2013'
            plt_data.print_choice_year_gas(year)   
        elif  year_option=='2014':
            year ='2014'
            plt_data.print_choice_year_gas(year)   
        elif  year_option=='2015':
            year ='2015'
            plt_data.print_choice_year_gas(year)   
        elif  year_option=='2016':
            year ='2016'
            plt_data.print_choice_year_gas(year)   
        elif  year_option=='2017':
            year ='2017'
            plt_data.print_choice_year_gas(year)   
        elif  year_option=='2018':
            year ='2018'
            plt_data.print_choice_year_gas(year)   
        elif  year_option=='2019':
            year ='2019'
            plt_data.print_choice_year_gas(year)   
        else :
            year ='2020'
            plt_data.print_choice_year_gas(year)   
    
    
    else: #radio else
        plt_data.print_everyyear_consumptionforoneoffamily()

        year_option = st.selectbox('年',
            ('2013','2014','2015','2016','2017','2018','2019','2020')
        )
        if year_option=='2013':
            year ='2013'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        elif  year_option=='2014':
            year ='2014'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        elif  year_option=='2015':
            year ='2015'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        elif  year_option=='2016':
            year ='2016'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        elif  year_option=='2017':
            year ='2017'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        elif  year_option=='2018':
            year ='2018'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        elif  year_option=='2019':
            year ='2019'
            plt_data.print_choice_year_gas_oneoffamily(year)   
        else :
            year ='2020'
            plt_data.print_choice_year_gas_oneoffamily(year)   
  

    '##### ➤ 很明顯的在 6 7 8 9 月(夏季) 瓦斯使用量偏低，在 12 1 2 3 月(冬季)時偏高'
    ''
    st.subheader('歷年與月平均溫度')
    month_v=st.slider("月份",1,12,6)
    plt_data.draw_tempure(month_v)
    ''
    rbt_plt_scottor=st.radio(
        "散佈圖-使用量與其他因素關係",("平均溫度","平均體感溫度","兩圖重和")
    )
    if rbt_plt_scottor == "平均溫度":
        '#### 溫度與使用量分布圖'
        plt_data.print_TXmean_and_gas()
    elif rbt_plt_scottor =="平均體感溫度":
        '#### 體感溫度與使用量分布圖'
        plt_data.print_RTmean_and_gas()
    else:
        '#### 體感溫度&溫度疊合'
        plt_data.print_RTmeantoTXmean()
    
    
    '##### ➤當溫度越高時，使用量明顯變低'
    ''
    st.subheader('相關係數')
    '##### 使用量與**溫度 體感溫度 風速 濕度**的相關係數'
    ld.print_data_corr()
    if st.button('熱圖'):
        plt_data.plot_data_figure_heatmap()
    


    '➤從相關係數發現 溫度 與 體感溫度 有高度的負相關，所以決定使用溫度與體感溫度來做機器學習與訓練'

elif sidebar=='機器學習':
    st.subheader("機器學習 線性回歸(Linear Resgression)")
    '#### 總使用量與溫度機器學習'
    choice_ML_predict = st.radio("平均溫度與體感溫度機器學習",
        ("月平均溫度","月平均體感溫度")
    )

    if choice_ML_predict=="月平均溫度":
        '##### X:平均溫度 Y:使用量 算出溫度與使用量的最佳方程式'
        ml_model.TXmean_and_gas_ml()
        v_tx = st.number_input('輸入想要推估的溫度(℃)')
        v_gas_tx = (-482543.05525943)*v_tx + 29876717.97914793
        vgstx_max = np.round((v_gas_tx+1191714.848)/1000000,3)
        vgstx_min = np.round((v_gas_tx-1191714.848)/1000000,3)
        if st.button('溫度推估使用量'):
            st.markdown('#### 當月溫度為'+str(v_tx)+'℃時，')
            st.markdown('#### 推估月總使用量為'+str(vgstx_min)+'~'+str(vgstx_max)+"(單位:百萬立方公尺)")


    else:
        '##### X:平均體感溫度 Y:使用量 算出體感溫度與使用量的最佳方程式'
        ml_model.RTmean_and_gas_ml()
        v_rt = st.number_input('輸入想要推估的體感溫度(℃)')
        v_gas_rt = (-365896.70973523)*v_rt + 27760988.330900572
        vgsrt_max= np.round((v_gas_rt+1201216.551)/1000000,3)
        vgsrt_min= np.round((v_gas_rt-1201216.551)/1000000,3)
        if st.button('體感溫度推估使用量'):
            st.markdown('#### 當月體感溫度為'+str(v_rt)+'℃時，')
            st.markdown('#### 推估月總使用量為'+str(vgsrt_min)+'~'+str(vgsrt_max)+"(單位:百萬立方公尺)")

    '#### 單一用戶與溫度機器學習'
    choice_ML_predict_onefamily = st.radio("單戶溫度與體感機器學習",
        ("月平均溫度","月平均體感溫度")
    )

    if choice_ML_predict_onefamily=="月平均溫度":
        '##### X:平均溫度 Y:使用量 算出溫度與使用量的最佳方程式'
        ml_model.ML_consumptionforoneoffamily_tx()
        #y = [-1.2349557]x + 76.72030411467331

        p_tx_one = st.number_input('輸入想要推估的溫度(℃)/單戶')
        p_gas_tx_one = (-1.2349557)*p_tx_one + 76.72030411467331
        pgstx_max = np.round((p_gas_tx_one+3.032),3)
        pgstx_min = np.round((p_gas_tx_one-3.032),3)
        if st.button('溫度推估單戶使用量'):
            st.markdown('#### 當月溫度為'+str(p_tx_one)+'℃時，')
            st.markdown('#### 推估月總使用量為'+str(pgstx_min)+'~'+str(pgstx_max)+"(單位:立方公尺)")


    else:
        '##### X:平均體感溫度 Y:使用量 算出體感溫度與使用量的最佳方程式'
        ml_model.ML_consumptionforoneoffamily_rt()
        #y = [-0.9359161]x + 71.2923200049654

        p_rt_one = st.number_input('輸入想要推估的體感溫度(℃)/單戶')
        p_gas_rt_one = (-0.9359161)*p_rt_one + 71.2923200049654
        pgsrt_max= np.round((p_gas_rt_one+3.078),3)
        pgsrt_min= np.round((p_gas_rt_one-3.078),3)
        if st.button('體感溫度推估單戶使用量'):
            st.markdown('#### 當月體感溫度為'+str(p_rt_one)+'℃時，')
            st.markdown('#### 推估月總使用量為'+str(pgsrt_min)+'~'+str(pgsrt_max)+"(單位:百萬立方公尺)")

    ''
    '▶ 選擇了**溫度**作為最後的使用量預測參數，因為TCCIP沒有體感溫度未來的資料'
    
    #### 體感溫度/溫度 與 使用量 分佈圖疊合'
    #ml_model.RtTx_and_gas_ml()



elif sidebar=='未來影響':
    st.subheader('在IPSL_CM5A_LR模組的環境下，RCP各情境的影響')
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

    RCP_choice = st.radio('選擇RCP情境',("RCP2.6", "RCP4.5","RCP6.0",'RCP8.5'))
    predict_year = st.slider('比較年分',2021,2099)


    month_select = st.selectbox(
        '月份',('1','2','3','4','5','6','7','8','9','10','11','12')
    )

    #count_reduce_infuture(month,pcrFile,p_year,RCP)
    if RCP_choice =="RCP2.6":
        dfload=df_pPCR26
        N="RCP2.6"
        txt.count_reduce_infuture(month_select,dfload,predict_year,N)
    elif RCP_choice =="RCP4.5":
        dfload=df_pPCR45
        N="RCP4.5"
        txt.count_reduce_infuture(month_select,dfload,predict_year,N)
    elif RCP_choice =="RCP6.0":
        dfload=df_pPCR60
        N="RCP6.0"
        txt.count_reduce_infuture(month_select,dfload,predict_year,N)
    else:
        dfload=df_pPCR85
        N="RCP8.5" 
        txt.count_reduce_infuture(month_select,dfload,predict_year,N)
    
    