import numpy as np
import pandas as pd
from PIL import Image


#画像表示編
#    st.write('Display Image')
#
#    img = Image.open('sample.PNG')
#
#    #Webアプリに絡むレイアウトを勝手に変えてくれる(use_column_width)
#    st.image(img, caption='SAMUNE',use_column_width=True)

#st.write('Display Image')

#動的な動作検証
#チェックボックスを作成(チェックあり：true, 無し：false)
#画像表示の切り替え
#if st.checkbox('Show Image'):
#    img = Image.open('sample.PNG')
#    st.image(img, caption='SAMUNE',use_column_width=True)

#セレクトボックス
#option = st.selectbox(
#    'あなたが好きな数字を教えてください。',
#    list(range(1,11))
#)
#'あなたの好きな数字は、', option,'です'

#st.sidebar.***：画面の左側に寄る
#text = st.sidebar.text_input('あなたの好きな趣味を教えてください。')
#slider：最小値,最大値、初期値
#condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
#text = st.text_input('あなたの好きな趣味を教えてください。')
#condition = st.slider('あなたの今の調子は？',0,100,50)
#'あなたの好きな趣味は',text
#'コンディション:',condition


#st.write('DataFrame')
#表を作ろう
    #df = pd.DataFrame({
    #    '1列目':[1,2,3,4],
    #    '2列目':[10,20,30,40]
    #})
    #dataframe 縦横の長さを指定できる(width=100,height=100)
    #writeでも可能。ただ、縦横の長さは指定できない。

    #axis = 0 (列の指定)
    #axis = 1 (行の指定)
    #表内でソートとかしたければdataframeを使用する。
    #st.dataframe(df.style.highlight_max(axis=0))

    #表を表示させたいときに使用する。
    #st.table(df.style.highlight_max(axis=0))

#グラフを作ろう

    #グラフを書く
    #df = pd.DataFrame(
    #    np.random.rand(20, 3),
    #    columns=['a','b','c']
    #)

    #折れ線グラフ
    #st.line_chart(df)
    #折れ線グラフの中をエリアで塗る
    #st.area_chart(df)
    #棒グラフ
    #st.bar_chart(df)

#マップにプロット(緯度経度)
#    df = pd.DataFrame(
#        np.random.rand(100,2)/[50,50] + [35.69,139.70],
#        columns=['lat','lon']
#    )
#    st.map(df)


#markupdown
#バッククォートの作り方：shiftキー + 「@」ボタン
#"""
## 章
### 節
#### 項
#
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""
