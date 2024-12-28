import streamlit as st
from mongodb.prompt_manager import get_prompt

def existing_prompt():
    user = st.session_state["user"]
    prompts = list(get_prompt(user["_id"]))

    if prompts == None:
        st.write("Add Prompt First!!")

    for prompt in prompts:
        st.write(prompt["user_questionaire"])
        st.write("\n" + prompt["prompt"])
        st.write("---------------------------------------------------------------------------------------")