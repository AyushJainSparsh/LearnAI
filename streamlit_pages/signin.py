import streamlit as st
from mongodb.signin import signin

# Signin Page
def Signin():
    st.title("Sign In")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    if st.button("Signin"):
        if signin(username , password):
            st.success(f"Welcome, {username}!")
            st.session_state.authenticated = True
            st.session_state.page = "prompt_manager"
        else:
            st.error("Invalid username or password.")        
    if st.button("Sign Up"):
        st.session_state.page = "signup"
