import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGODB_URI'))
db = client[os.getenv('DB_NAME')]
books_collection = db['books']

# Your existing books list
books_list = [
    {"id": 0, "author": "guy 0", "language": "english", "title": "title 0"},
    {"id": 1, "author": "guy 1", "language": "english", "title": "title 1"},
    {"id": 2, "author": "guy 2", "language": "german", "title": "title 2"},
    {"id": 3, "author": "guy 3", "language": "english", "title": "title 3"},
]

# Insert books into the collection
if books_collection.count_documents({}) == 0:
    books_collection.insert_many(books_list)
    print("Books have been inserted into the database.")
else:
    print("The collection already contains data.")
