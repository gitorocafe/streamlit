import streamlit as st
import time


st.title('RC梁検討')
'''
## RC構造設計規準・同解説 2010年版
'''


if st.checkbox('Show Image'):
    st.write('Hello Streamlit')

#option = st.selectbox('あなたの好きな数字は', list(range(1,11)))

#st.write('あなたの好きな数字は',option,'です')

st.write('インタラクティブ')
option = st.text_input('あなたの趣味を教えてください。')
option,'です'

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    bar.progress(i+1)
    latest_iteration.text(i+1)
    time.sleep(0.05)