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
all_df = pd.read_csv('201302 to 2020_all2.csv')
sw_df = pd.read_csv('sw_data.csv')
# Show first data 
''



#圓餅圖
def piechart():
    plot_area = st.empty()
    labels = 'Gas', 'Device', 'Rent', 'Communication','Other'
    sizes = [77, 13, 7, 2 , 1]
    explode = (0.1, 0, 0, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=55)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    legend = ax1.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(fig1)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
lm = LinearRegression()
def RXmean_and_gas_ml():
    
    all_df = pd.read_csv('201302 to 2020_all2.csv')
    X = all_df['RT-mean']
    y = all_df['Consumption(m^3)']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state =22) 

    X_train = np.array(x_train)
    X_train = X_train.reshape(-1,1)

    X_test = np.array(x_test)
    X_test = X_test.reshape(-1,1)

    txmean_fit = lm.fit(X_train, y_train)
    st.write('線性回歸方程式為 : ')
    string = 'y = ' + str(txmean_fit.coef_) + 'x + ' + str(txmean_fit.intercept_)
    st.text(string)
    Y_train = lm.predict(X_train)
    mse1 = sqrt(mean_squared_error(y_train, lm.predict(X_train)))
    mse2 = sqrt(mean_squared_error(y_test, lm.predict(X_test)))
    st.text('使用量(m^3)誤差 : train_RMSE= {:.3f}, test_RMSE = {:.3f} '.format(mse1,mse2) )
    
    R2_train = lm.score(X_train,y_train)
    R2_test = lm.score(X_test,y_test)
    st.text('預測準確度(score) train_R2 = {:.3f}, test_R2 = {:.3f} '.format(R2_train,R2_test))


    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))

    ax.scatter(x_train,y_train, c='b')
    ax.plot(x_train,Y_train,'navy')
    ax.set_xlabel('Temperature(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    
    plot_area.pyplot(f)

def RtTx_and_gas_ml():
    
    all_df = pd.read_csv('201302 to 2020_all2.csv')
    X1 = all_df['TX-mean']
    X2 = all_df['RT-mean']
    y = all_df['Consumption(m^3)']

    x_train, x_test, y_train, y_test = train_test_split(X1, y, test_size = 0.3, random_state =22) 
    x_train1, x_test1, y_train1, y_test1 = train_test_split(X2, y, test_size = 0.3, random_state =22) 

    X_train = np.array(x_train)
    X_train = X_train.reshape(-1,1)

    X_train1 = np.array(x_train1)
    X_train1 = X_train1.reshape(-1,1)

    X_test = np.array(x_test)
    X_test = X_test.reshape(-1,1)

    X_test1 = np.array(x_test1)
    X_test1 = X_test1.reshape(-1,1)

    txmean_fit = lm.fit(X_train, y_train)
    rxmean_fit = lm.fit(X_train1, y_train1)
    
    Y_train = lm.predict(X_train)
    Y_train1 = lm.predict(X_train1)



    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))

    ax.scatter(x_train,y_train, c='b')
    ax.plot(x_train,Y_train,c='navy',label ="TX")

    ax.scatter(x_train1,y_train1, c='c')
    ax.plot(x_train1,Y_train1,c='c', label = "RT")

    ax.set_xlabel('Temperature(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    
    plot_area.pyplot(f)



#選單
sidebar = st.sidebar.selectbox(
    "快速選單",
    ("大台北簡介", "資料集和資料視覺化", "機器學習","未來影響")
)

if sidebar=='大台北簡介':
    st.subheader('大台北業務項目 201112~202109 平均比例')
    #plt_data.piechart()
    piechart()
    #選擇測站資料
    ''
    '#### 大台北主要服務地區分佈在：' 
    '##### 松山、信義、大安、大同、萬華、中正、中山、士林'
    st.image('測站位置圖.png', caption='StNO postion')
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
    RXmean_and_gas_ml()
    '#### 體感溫度/溫度 與 使用量 分佈圖疊合'
    RtTx_and_gas_ml()