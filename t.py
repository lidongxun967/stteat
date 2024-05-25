import streamlit as st
import pandas as pd
import os

# 定义 CSV 文件的路径
CSV_FILE_PATH = 'data_storage.csv'

# 初始化或读取 CSV 文件
if os.path.exists(CSV_FILE_PATH):
    data_df = pd.read_csv(CSV_FILE_PATH)
else:
    data_df = pd.DataFrame(columns=['data'])

# 定义一个函数来添加数据到 CSV 文件
def add_data_to_csv(item):
    global data_df
    new_data = pd.DataFrame({'data': [item]})
    data_df = pd.concat([data_df, new_data], ignore_index=True)
    data_df.to_csv(CSV_FILE_PATH, index=False)

# Streamlit 应用布局
st.title('跨会话数据存储器')

# 输入框让用户输入数据
new_item = st.text_input('输入你想存储的数据：')

# 按钮触发添加数据到存储器
if st.button('添加数据'):
    if new_item:
        add_data_to_csv(new_item)
        st.success(f'成功添加数据: {new_item}')
    else:
        st.error('请输入有效数据')

# 显示当前存储的所有数据
st.subheader('存储的数据')
st.write(data_df)

# 添加一个清除数据的功能
if st.button('清除所有数据'):
    if os.path.exists(CSV_FILE_PATH):
        os.remove(CSV_FILE_PATH)
        data_df = pd.DataFrame(columns=['data'])
        st.success('所有数据已清除')
    else:
        st.error('没有数据可以清除')
