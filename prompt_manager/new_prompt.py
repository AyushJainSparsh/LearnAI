import streamlit as st
from gemini.questions import get_questions
from gemini.prompt_maker import get_prompt
from mongodb.prompt_manager import add_prompt

def new_prompt():
    rough_prompt = st.text_input("Enter Rough Prompt!!")

    if st.button("Get Prompt"):
        questions = get_questions(rough_prompt)
        st.session_state.questions = questions
        st.session_state.question_idx = 0

    if 'questions' in st.session_state and st.session_state.question_idx < len(st.session_state.questions):
        current_question = st.session_state.questions[st.session_state.question_idx]
        current_answer = st.text_input(current_question["questions"], key=f"question_{st.session_state.question_idx}")
        
        if st.button("Next Question", key=f"next_button_{st.session_state.question_idx}"):
            st.session_state.questions[st.session_state.question_idx]["answer"] = current_answer
            st.session_state.question_idx += 1

    if 'questions' in st.session_state and st.session_state.question_idx >= len(st.session_state.questions):
        input_text = "Rough Prompt : " + rough_prompt + " \n"
        for question in st.session_state.questions:
            input_text += " \n " + "Question : " + question["questions"] + " \n " + "Answer : " + question["answer"] + " \n"
        
        if st.button("Get Well Prompt", key="get_well_prompt"):
            prompt = get_prompt(input_text)
            st.write("Prompt : " + prompt)
            user = st.session_state["user"]
            add_prompt(user_id=user["_id"], data=input_text, prompt=prompt)

            # Clear specific session state keys
            del st.session_state['questions']
            del st.session_state['question_idx']

    try:
        new_prompt()
    except Exception as e:
        st.warning("Error: " + str(e))
