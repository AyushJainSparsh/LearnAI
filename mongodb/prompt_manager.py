from utils.mongodb_client import get_promptdb

def add_prompt(user_id , data , prompt):
    prompt_collection = get_promptdb()
    prompt_collection.insert_one({"user_id" : user_id , "user_questionaire" : data , "prompt" : prompt})


def get_prompt(user_id):
    prompt_collection = get_promptdb()
    return prompt_collection.find({"user_id" : user_id})