import typing_extensions as typing
from utils.gemini_client import get_gemini_model as get_model

def get_prompt(task):
    model = get_model()

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",  # Adjust to "system" or "user" based on your need
                "parts": [
                    {"text": '''
                    You're a prompt engineer and user have no knowledge of prompt engineering and don't know how to write a prompt.
                    you will get  a task and question answer based on that task.
                    you have to create a prompt so that user used that prompt to reach that goal.
                    '''
                    }
                ]
            }
        ]
    )
    try:
        response = chat_session.send_message(task)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return "Error: Unable to generate recommendation.Try again!!"