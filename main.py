import streamlit as st
from streamlit_pages.signin import Signin
from streamlit_pages.signup import Signup
from streamlit_pages.prompt_manager import prompt_manager

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "page" not in st.session_state:
    st.session_state.page = "signin"

if st.session_state.page == "signin":
    Signin()
elif st.session_state.page == "signup":
    Signup()

# If authenticated, display the main app
elif st.session_state.authenticated:
    prompt_manager()