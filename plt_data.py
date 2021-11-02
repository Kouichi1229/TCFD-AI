import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

#讀入資料
all_df = pd.read_csv('201302 to 2020_all2.csv')
sw_df = pd.read_csv('sw_data.csv')

#主要服務比例 圓餅圖
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
 
 

#只取 使用量 與 年月份關係 / 切割資料 每年 
gas_2013 = all_df['Consumption(m^3)'][:11]
gas_2014 = all_df['Consumption(m^3)'][11:23]
gas_2015 = all_df['Consumption(m^3)'][23:35]
gas_2016 = all_df['Consumption(m^3)'][35:47]
gas_2017 = all_df['Consumption(m^3)'][47:59]
gas_2018 = all_df['Consumption(m^3)'][59:71]
gas_2019 = all_df['Consumption(m^3)'][71:83]
gas_2020 = all_df['Consumption(m^3)'][83:95]



# 201302~2020 月份與使用量折線圖
def print_everyyear_gas():
    # グラフを書き出すためのプレースホルダを用意する
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(10,4))
    ax.plot( all_df['Month'][:11], gas_2013, 'r.-', alpha=0.7, linewidth=2, label='2013')
    ax.plot( all_df['Month'][11:23], gas_2014, 'g.-', alpha=0.7, linewidth=2, label='2014')
    ax.plot( all_df['Month'][23:35], gas_2015, 'b.-', alpha=0.7, linewidth=2, label='2015')
    ax.plot( all_df['Month'][35:47], gas_2016,  'y.-', alpha=0.7, linewidth=2, label='2016')
    ax.plot( all_df['Month'][47:59], gas_2017,  'c.-', alpha=0.7, linewidth=2, label='2017')
    ax.plot(all_df['Month'][59:71], gas_2018,  'm.-', alpha=0.7, linewidth=2, label='2018')
    ax.plot(all_df['Month'][71:83], gas_2019,  'r.-', alpha=0.7, linewidth=2, label='2019')
    ax.plot(all_df['Month'][83:95], gas_2020,  'g.-', alpha=0.7, linewidth=2, label='2020')
    ax.set_xlabel('Month')
    ax.set_ylabel('Make use of gas(m^3)')
    
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

#畫出溫度和使用量分布圖
def print_TXmean_and_gas():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))

    ax.plot(all_df['TX-mean'], all_df['Consumption(m^3)'], 'c.', label='Temperature')

    ax.set_xlabel('Temperature(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

    #畫出體感溫度和使用量分布圖
def print_RTmean_and_gas():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))

    ax.plot(all_df['RT-mean'], all_df['Consumption(m^3)'], 'b.', label='RT')

    ax.set_xlabel('RT(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

#畫出疊合分布圖
def print_RTmeantoTXmean():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))

    ax.plot(all_df['TX-mean'], all_df['Consumption(m^3)'], 'c.', label='Temperature')
    ax.plot(all_df['RT-mean'], all_df['Consumption(m^3)'], 'b.', label='RT')

    ax.set_xlabel('Temperature(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)



