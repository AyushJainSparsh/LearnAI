import streamlit as st
from mongodb.signup import signup

def Signup():
    st.title("Signup")
    username = st.text_input("Enter a username")
    password = st.text_input("Enter a password", type="password")
    if st.button("Signup"):
        if signup(username , password):
            st.session_state.page = "signin"
            st.success("Signup successful! You can now sign in.")
        else :
            st.warning("Username already exists. Please choose a different username.")