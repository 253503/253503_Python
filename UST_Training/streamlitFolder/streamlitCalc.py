import streamlit as st

st.title("Calculator Demo")

option = st.selectbox(
        "Select your numerical operation",
        ("Add","Subtract","Multiply","Divide"),
)

st.write("your selected:",option)


num1 = st.text_input("Number 1:")
st.write("Input Number1",num1)

num2 = st.text_input("Number 2:")
st.write("Input Number2",num2)


if(option=="Add"):
    result = int(num1)+int(num2)
    st.text(result)

if(option=="Subtract"):
    result = int(num1)-int(num2)
    st.text(result)

if(option=="Multiply"):
    result = int(num1)*int(num2)
    st.text(result)

if(option=="Divide"):
    result = int(num1)/int(num2)
    st.text(result)