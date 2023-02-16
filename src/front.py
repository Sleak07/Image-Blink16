# for making the web interface app
import streamlit as st

# making a selectbox for selecting options
option = st.selectbox("What you want to do", ("sharp", "bright", "dark"))
st.write('You selected:', option)