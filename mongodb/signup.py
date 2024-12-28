import hashlib
from utils.mongodb_client import get_usersdb
import streamlit as st

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username ,password ):
    users_collection = get_usersdb()
    if users_collection.find_one({"username" : username}):
        print("Username already exists, Please choose different name.")
        return False
    else:
        hashed_password = hash_password(password)
        users_collection.insert_one({"username" : username , "password" : hashed_password})
        return True