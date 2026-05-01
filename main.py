import streamlit as st
st.title("My First Streamlit App")
name=st.text_input("Enter your name:")
if st.button("submit"):
    st.write("Hello!{name}Welcome to  Streamlit.")
