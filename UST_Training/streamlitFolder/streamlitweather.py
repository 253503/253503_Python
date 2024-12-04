import requests
import streamlit as st
import time

st.title("Weather forecast")
lantitude=st.text_input("latitude:")
longitude=float(st.text_input("longitude:"))

#12.9719
#77.5937

url = "https://api.open-meteo.com/v1/forecast"
params ={
    "latitude":lantitude,
    "longitude":longitude,
    "current_weather":"true"
        }

response = requests.get(url,params)
st.write(response)
#st.write(response.json()['current_weather'])
st.write(response.json()['current_weather']['temperature'])


         
