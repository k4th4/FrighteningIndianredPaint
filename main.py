import streamlit as st 
import pandas as pd



df = pd.read_csv('CAD_data_2021-11-24.csv')



st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App.
Enjoy it!
''')
st.write(df)


myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)
