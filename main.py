import streamlit as st


st.title('RC梁検討')
'''
## RC構造設計規準・同解説 2010年版
'''

#単位
units_dic = {
    'mm' : 'mm',
    'cm' : 'cm',
    'm' : 'm',
    'mm2': 'mm2',
    'N/mm2' : 'N/mm2',
    '本':'本'
}

#鉄筋径
bar_Dia = (
    'D10',
    'D13',
    'D16',
    'D19',
    'D22',
    'D25',
    'D29'
)


#設計条件
width = st.number_input('梁巾 B (' + units_dic['mm'] +')', 0, 1000, 0)
depth = st.number_input('梁せい D (' + units_dic['mm'] +')', 0, 2000, 0)
Fc = st.selectbox('コンクリートの設計基準強度 Fc (' + units_dic['N/mm2']+')',(18,21,24,27,30,33,36,39,42,45,48,51,54,57,60))

#上端主筋
option_top = st.selectbox('上端主筋径：', list(bar_Dia))
nos_top1 = st.number_input('1段目鉄筋本数：' + units_dic['本'], 0, 10, 0)
nos_top2 = st.number_input('2段目鉄筋本数：' + units_dic['本'], 0, 10, 0)

#下端主筋
option_bottom = st.selectbox('下端主筋径：', list(bar_Dia))
nos_bottom1 = st.number_input('1段目鉄筋本数：' + units_dic['本'], 0, 10, 0)
nos_bottom2 = st.number_input('2段目鉄筋本数：' + units_dic['本'], 0, 10, 0)

area = width * depth
st.write('断面積 A：{:<20,.1f}'.format(area),units_dic['mm2'])