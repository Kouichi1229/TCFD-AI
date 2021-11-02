# draw pie chat 

def piechart_revenue():
    plot_area = st.empty()
    labels = 'Gas', 'Device', 'Rent', \
    'Communication','Other'
    sizes = [77, 13, 7, 2 , 1]
    explode = (0.1, 0, 0, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=55)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    legend = ax1.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(fig1)
#plt_data.pieChart_Revenue()
piechart_revenue() 

""" 
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


st.subheader("機器學習 線性回歸(Linear Resgression)")
'#### X:平均溫度 Y:使用量 算出溫度與使用量的最佳方程式'
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt


lm = LinearRegression()

# Loading data 
# Data	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	Month	RH-mean	TX-mean	WD-mean	RT-mean
#all_df = pd.read_csv('201302 to 2020_all2.csv')
#sw_df = pd.read_csv('sw_data.csv')


def TXmean_and_gas_ml():
    
    all_df = pd.read_csv('201302 to 2020_all2.csv')
    X = all_df['TX-mean']
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

    ax.scatter(x_train,y_train, c='c')
    ax.plot(x_train,Y_train,'royalblue')
    ax.set_xlabel('Temperature(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    
    plot_area.pyplot(f)

TXmean_and_gas_ml() """