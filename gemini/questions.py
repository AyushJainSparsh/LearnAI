import typing_extensions as typing
from utils.gemini_client import get_gemini_model as get_model
import json

class Questionaire(typing.TypedDict):
    questions : str

def get_questions(task):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
        "response_schema" : list[Questionaire]
    }

    model = get_model(generation_config)

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",  # Adjust to "system" or "user" based on your need
                "parts": [
                    {"text": '''
                    You're a prompt engineer and user have no knowledge of prompt engineering and don't know how to write a prompt.
                    the user will give you a task and based on these tasks you can ask some questions based on that task and you have 
                    to prepare a best prompt for it so that user can use it for their goal.

                    the output should be in the form of question json list .
                    questions is an string list of the questions you can ask with user. 
                    '''
                    }
                ]
            }
        ]
    )
    try:
        response = chat_session.send_message(task)
    except Exception as e:
        print(f"Error: {e}")
        return "Error: Unable to generate recommendation.Try again!!"
    
    
    output = json.loads(response.text)
    return output
