from numpy import loads
import streamlit as st
import pandas as pd
import numpy as np

load='file_csv/'
#C:\Users\user\Desktop\大作業\大台北TCFD整合\file_csv\standard_Consumption .csv
#C:\Users\user\Desktop\大作業\大台北TCFD整合\file_csv\RCP2_6predict.csv
df_standard = pd.read_csv(load+'standard_Consumption .csv')




def print_movition():
    
    txt = st.text_area('企劃動機與目的', '''
      自20世紀以來，人類文明快速的發展，同時也帶來嚴重的氣候影響。在全球暖化、氣溫上升的情況下，連帶產生北極融冰、海平面上升、各地極端天氣等等的問題。
    因此在2015年，國際金融穩定委員會成立了氣候相關財務揭露（Task Force on Climate-related Financial Disclosures，後簡稱TCFD）工作小組。TCFD的目的
    在於擬定一套氣候相關的財務資訊揭露建議，將未來氣候所帶來的風險以及機會提供給投資者以及決策者。近年來，由於極端天氣事件在全球不斷發生，因此TCFD的概念
    也越來越被重視。而在台灣，雖然目前沒有強制的法規規定企業需要提供TCFD報告，但也有越來越多的投資者希望企業主動提供報告，告知未來氣候可能帶來的風險以及
    轉機。目前部分企業雖然有提供TCFD報告，內容卻大多只提及如何在企業內做到環保減碳，鮮少提出未來氣候對企業的實際影響以及企業的應對作為。
        本次提案按照TCFD的目標，針對大台北區瓦斯股份有限公司（以下簡稱大台北瓦斯）近十年的營收進行分析，探討營收變化和氣候狀況的相關性，並利用未來氣候的
    模擬資料，使用機器學習方法推估該未來情境下的天然氣使用量變化和獲利情形，嘗試了解天然氣使用習慣與氣候的關聯性，以及未來的氣候情境下，天然氣使用量變化所
    導致企業營收的改變。並建立一套可以推估台灣天然氣產業使用情況的模型。而提案的結果也可以提供大台北瓦斯更完整的TCFD報告，以應對投資人、客戶以及社會對企業
    的期待。
     ''')
    st.write(txt)


#p_consumption=predict_dt[predict_dt['Date']==203401]['consumption']
#計算與標準差了多少
def count_reduce_infuture(month,pcrFile,p_year,RCP):
    standard = df_standard[df_standard['Month']==int(month)]['Consumption-mean']
    standard = pd.to_numeric(standard, errors='coerce')
    standard = float(standard)/1000000
    if int(month) < 10:
        month= '0'+str(month)
    else:
        month=str(month)
    p_data = str(p_year) + str(month)
    main_dt = pcrFile[pcrFile["Date"]==int(p_data)]['consumption']
    main_dt = pd.to_numeric(main_dt, errors='coerce')
    main_dt = float(main_dt)/1000000
    result = np.round(abs(main_dt-standard),3)
    #Revenue

    st.markdown('當在'+RCP+'的情境下,在'+str(p_year)+'年'+str(month)+'月時,跟過去'+str(month)+'月的平均使用量相比')
    st.markdown('減少了{:.2%}的使用量'.format(result)+'(百萬立方公尺)')
    #st.markdown('')