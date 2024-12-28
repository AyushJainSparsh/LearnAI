from pymongo import MongoClient
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

def get_client():
    URI = st.secrets["MONGODB_URI"]
    client = MongoClient(URI , tls = True , tlsAllowInvalidCertificates = False)
    return client["learn-ai"]

def get_promptdb():
    db = get_client()
    return db["prompt_task"]

def get_usersdb():
    db= get_client()
    return db["users"]