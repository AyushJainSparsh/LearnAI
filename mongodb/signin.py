import hashlib
from utils.mongodb_client import get_usersdb
import streamlit as st

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signin(username , password):
    users_collection = get_usersdb()
    user = users_collection.find_one({"username":username})
    if user and user["password"] == hash_password(password):
        st.session_state["user"] = user  # Store user details in session
        return True
    else:
        return False