import streamlit as st

st.title("Input Demo")
#st.title("_Streamlit_ is :blue[cool] :sunglasses:")


username = st.text_input("Username")
st.write("Input Username",username)

Password = st.text_input("Password")
st.write("Input Password",Password)
