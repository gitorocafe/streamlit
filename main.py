import streamlit as st
#import numpy as np
#import pandas as pd
import time


st.title('streamlit 超入門desuka')


if st.checkbox('Show Image'):
    st.write('あはは')

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

'''
# markdown記法のテスト
## テスト
### テスト

'''