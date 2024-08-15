import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def connect():
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client[os.getenv('DB_NAME')]
    return db

def createUser(user): 
    db = connect()
    user_connection = db['users']
    return user_connection.insert_one(user)

def getUserByUsername(username):
    db = connect()
    user_connection = db['users']
    return user_connection.find_one({"username": username})

def updateUser(username, update_data):
    db = connect()
    user_connection = db['users']
    result = user_connection.update_one({"username": username}, {"$set": update_data})

def deleteUser(username):
    db = connect()
    user_connection = db['users']
    result = user_connection.delete_one({"username": username})
