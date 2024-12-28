import streamlit as st
from streamlit_option_menu import option_menu
from prompt_manager.new_prompt import new_prompt
from prompt_manager.existing_prompt import existing_prompt

def prompt_manager():
    st.title("Prompt Manager")
    work = option_menu(
        menu_title="Prompt Manager",
        options=["New Prompt" , "Existing Prompt"]
    )

    if work == "New Prompt":
        new_prompt()
    if work == "Existing Prompt":
        existing_prompt()

    if st.button("LogOut"):
        st.session_state.clear()