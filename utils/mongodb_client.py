from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    URI = "mongodb+srv://ayushjainsparsh2004ajs:Learn-AI-AJS@learn-ai.2nkjs.mongodb.net/?retryWrites=true&w=majority&appName=Learn-AI"
    client = MongoClient(URI , tls = True , tlsAllowInvalidCertificates = False)
    return client["learn-ai"]

def get_promptdb():
    db = get_client()
    return db["prompt_task"]

def get_usersdb():
    db= get_client()
    return db["users"]