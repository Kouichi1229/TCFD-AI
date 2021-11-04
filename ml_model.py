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
# Data	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	
# Month	RH-mean	TX-mean	WD-mean	RT-mean
#all_df = pd.read_csv('201302 to 2020_all2.csv')
#sw_df = pd.read_csv('sw_data.csv')

#溫度與使用量ML
def TXmean_and_gas_ml():
    
    all_df = pd.read_csv('file_csv/201302 to 2020_all2.csv')
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

#平均體感溫度與使用量ML
def RTmean_and_gas_ml():
    
    all_df = pd.read_csv('file_csv/201302 to 2020_all2.csv')
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


# 平均體感和平均溫度 合在一起的圖
def RtTx_and_gas_ml():
    
    all_df = pd.read_csv('file_csv/201302 to 2020_all2.csv')
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
