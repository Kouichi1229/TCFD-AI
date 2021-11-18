import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#讀入資料
load='file_csv/'
all_df = pd.read_csv(load + '201302 to 2020_all2.csv')
sw_df = pd.read_csv(load + 'sw_data.csv')
bf_dt = pd.read_csv(load +'2014to2020gas.csv')
df_PCR26 = pd.read_csv(load +'RCP2_6_year.csv')
df_PCR45 = pd.read_csv(load +'RCP4_5_year.csv')
df_PCR60 = pd.read_csv(load +'RCP6_0_year.csv')
df_PCR85 = pd.read_csv(load +'RCP8_5_year.csv')
df_pPCR26 =pd.read_csv(load +'RCP2_6predict.csv')
df_pPCR45 =pd.read_csv(load +'RCP4_5predict.csv')
df_pPCR60 =pd.read_csv(load +'RCP6_0predict.csv')
df_pPCR85 =pd.read_csv(load +'RCP8_5predict.csv')
df_C_standard = pd.read_csv(load+'standard_Consumption .csv')
df_subscriber = pd.read_csv(load +'subscriber_number.csv')
bf_dt_oneoffamily = pd.read_csv(load +'2014to2020oneoffamily.csv')
#RCP2.6_yearoneoffamily.csv
df_PCR26_oneoffamily = pd.read_csv(load +'RCP2.6_yearoneoffamily.csv')
df_PCR45_oneoffamily = pd.read_csv(load +'RCP4.5_yearoneoffamily.csv')
df_PCR60_oneoffamily = pd.read_csv(load +'RCP6.0_yearoneoffamily.csv')
df_PCR85_oneoffamily = pd.read_csv(load +'RCP8.5_yearoneoffamily.csv')



# 欄位 : Date	Unit-price(TWD/m^3) 	Revenue(Billion)	Sticker-price(TWD/m^3)	Consumption(m^3)	 gross margin(1 million)	
#        Month	RH-mean	TX-mean	WD-mean	AT-mean Consumption for one of family(m^3)


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

# 201302~2020 月份與使用量折線圖
def print_everyyear_gas():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(10,4))
    ax.plot(all_df['Month'][:11], all_df['Consumption(m^3)'][:11], label='2013')
    for i in range(11,len(all_df['Month'])+1,12):
        if i < len(all_df['Month']):
            year = 2014 + (i//12)
            ax.plot( all_df['Month'][i:i+12], all_df['Consumption(m^3)'][i:i+12], label=str(year))

    ax.set_xlabel('Month')
    ax.set_ylabel('Make use of gas(m^3)')
    
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

# 201302~2020 月份與單戶使用量折線圖
def print_everyyear_consumptionforoneoffamily():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(10,4))
    ax.plot(all_df['Month'][:11], all_df['Consumption for one of family(m^3)'][:11], label='2013')
    for i in range(11,len(all_df['Month'])+1,12):
        if i < len(all_df['Month']):
            year = 2014 + (i//12)
            ax.plot( all_df['Month'][i:i+12], all_df['Consumption for one of family(m^3)'][i:i+12], label=str(year))

    ax.set_xlabel('Month')
    ax.set_ylabel('Make use of gas /one of family(m^3)')
    
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)



# 201302~2020 月份與使用量折線圖  單選項
def print_choice_year_gas(year):
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(10,4))

    if year =='2013':
        ax.plot(all_df['Month'][:11], all_df['Consumption(m^3)'][:11], 'y', label='2013')
    else:
        all_df.index = all_df['Date']
        df_year = all_df.filter(like=str(year),axis=0)
        ax.plot(df_year['Month'],df_year['Consumption(m^3)'], 'y', label= str(year))

    ax.set_xlabel('Month')
    ax.set_ylabel('Make use of gas(m^3)')
    
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

# 201302~2020 月份與單用戶使用量折線圖  單選項
def print_choice_year_gas_oneoffamily(year):
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(10,4))

    if year =='2013':
        ax.plot(all_df['Month'][:11], all_df['Consumption for one of family(m^3)'][:11], 'y', label='2013')
    else:
        all_df.index = all_df['Date']
        df_year = all_df.filter(like=str(year),axis=0)
        ax.plot(df_year['Month'],df_year['Consumption for one of family(m^3)'], 'y', label= str(year))

    ax.set_xlabel('Month')
    ax.set_ylabel('Make use of gas/one of family(m^3)')
    
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

    ax.plot(all_df['AT-mean'], all_df['Consumption(m^3)'], 'b.', label='AT')

    ax.set_xlabel('AT(℃)')
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
    ax.plot(all_df['AT-mean'], all_df['Consumption(m^3)'], 'b.', label='AT')

    ax.set_xlabel('Temperature(℃)')
    ax.set_ylabel('Make use of gas(m^3)')
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

#PCR 與累積使用量圖 全部
def draw_all_pcr():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    ax.plot(bf_dt['Year'],bf_dt['Consumption(year)'],label='before')
    ax.plot(df_PCR26['Year'],df_PCR26['Consumption(year)'],label='RCP2.6')
    ax.plot(df_PCR45['Year'],df_PCR45['Consumption(year)'],label='RCP4.5')
    ax.plot(df_PCR60['Year'],df_PCR60['Consumption(year)'],label='RCP6.0')
    ax.plot(df_PCR85['Year'],df_PCR85['Consumption(year)'],label='RCP8.5')

    ax.set_xlabel('Year')
    ax.set_ylabel('make use of gas')

    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

# 選擇 PCR 單一線條圖
def draw_pcr(dfload,N):
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    ax.plot(bf_dt['Year'],bf_dt['Consumption(year)'],label='before')
    ax.plot(dfload['Year'],dfload['Consumption(year)'],label=N)

    ax.set_xlabel('Year')
    ax.set_ylabel('make use of gas')

    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

#PCR 與單戶使用量圖 全部
def draw_all_pcr_oneodfamily():
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    ax.plot(bf_dt_oneoffamily['Year'],bf_dt_oneoffamily['Consumption/one of family(year)'],label='before')
    ax.plot(df_PCR26_oneoffamily['Year'],df_PCR26_oneoffamily['Consumption(year)'],label='RCP2.6')
    ax.plot(df_PCR45_oneoffamily['Year'],df_PCR45_oneoffamily['Consumption(year)'],label='RCP4.5')
    ax.plot(df_PCR60_oneoffamily['Year'],df_PCR60_oneoffamily['Consumption(year)'],label='RCP6.0')
    ax.plot(df_PCR85_oneoffamily['Year'],df_PCR85_oneoffamily['Consumption(year)'],label='RCP8.5')

    ax.set_xlabel('Year')
    ax.set_ylabel('make use of gas/ one of family(M^3)')

    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

# 選擇 PCR 單一線條圖  單戶
def draw_pcr_oneodfamily(dfload,N):
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    ax.plot(bf_dt_oneoffamily['Year'],bf_dt_oneoffamily['Consumption/one of family(year)'],label='before')
    ax.plot(dfload['Year'],dfload['Consumption(year)'],label=N)

    ax.set_xlabel('Year')
    ax.set_ylabel('make use of gas/ one of family(M^3)')

    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)







# 不同年份 同月累積使用量長條圖
def plt_Consumption_month_bar(month):
    df = all_df[all_df['Month']==month]
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    x=df['Date']
    y=df['Consumption(m^3)']
    ax.bar(x, y, color="orange")
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)
#不同年份 同月單戶使用量長條圖
def plt_oneoffamily_month_bar(month):
    df = all_df[all_df['Month']==month]
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    x=df['Date']
    y=df['Consumption for one of family(m^3)']
    ax.bar(x ,y, color="yellow")
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)

# 不同年份 同月 溫度比較
def draw_tempure(month):
    plot_area = st.empty()
    f, ax = plt.subplots(1,1,figsize=(8,5))
    df = all_df[all_df['Month']==month]
    ax.plot(df['Date'], df['TX-mean'], 'r')
    

    ax.set_xlabel('Date-Year')
    ax.set_ylabel('Temperature(℃)')

    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    plot_area.pyplot(f)
# 相關係數感熱圖
def plot_data_figure_heatmap():
    df=all_df
    corr_data_set = ['Consumption(m^3)','RH-mean','TX-mean','WD-mean','AT-mean']
    fig = plt.figure()
    sns.heatmap(df[corr_data_set].corr(),annot=True,cmap='Blues')
    st.pyplot(fig)

