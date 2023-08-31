import streamlit as st
import pandas as pd

st.title('Demo streamlit app')

st.write('Hello world')
st.write(pd.DataFrame({
    'first_column':[1,2,3,4],
    'second_column':[10,20,30,40]
}))