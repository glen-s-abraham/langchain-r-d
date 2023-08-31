import streamlit as st
import pandas as pd

name = st.text_input('Your name')
if name:
    st.write(f'Hello {name}') 

x= st.number_input('Enter a number',min_value=1,max_value=99,step=1)
st.write(f'The current is {x}')

clicked = st.button('Click me!')
if clicked:
    st.write(':ghost:'*3)

agree = st.checkbox('I agree')
if agree:
    'Great, You agree'

checked = st.checkbox('Continue',value=True)
if checked:
    ':+1:'*5
df = pd.DataFrame({'Name':['glen','jenson','dougla'],'Age':[30,25,40]})

if st.checkbox('Show data'):
    st.write(df)

pets = ['cats','dogs','fish','turtle']
pet = st.radio('Favourite pets',pets,index=0,key='fav_pet')
st.write(f'Your favourite pet is {st.session_state.fav_pet}')

cities = ['London','Berlin','Paris','New york']
city = st.selectbox('Your city',cities)
st.write(f'You live in {city}')

