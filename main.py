import streamlit as st
import time


st.title('RC梁検討')
'''
## RC構造設計規準・同解説 2010年版
'''


# if st.checkbox('Show Image'):
#     st.write('Hello Streamlit2')





units_dic = {
    'mm' : 'mm',
    'cm' : 'cm',
    'm' : 'm',
    'N/mm2' : 'N/mm2',
    '本':'本'
}


st.write('インタラクティブ')
# 数値入力
width = st.number_input('梁巾 B：' + units_dic['mm'], 0, 2000, 0)
#width = st.text_input('梁巾 B：' + units_dic['mm'])
depth = st.text_input('梁せい D：' + units_dic['mm'])
Fc = st.text_input('コンクリートの設計基準強度 Fc：' + units_dic['N/mm2'])

bar_Dia = (
    'D10',
    'D13',
    'D16',
    'D19',
    'D22',
    'D25',
    'D29'
)

option = st.selectbox('鉄筋径：', list(bar_Dia))
nos = st.text_input('1段目鉄筋本数：' + units_dic['本'])

#st.write('あなたの好きな数字は',option,'です')

# st.write('プログレスバーの表示')
# 'start!!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     bar.progress(i+1)
#     latest_iteration.text(i+1)
#     time.sleep(0.05)