import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv('MONGODB_URI'))
db = client[os.getenv('DB_NAME')]
books_collection = db['books']

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books = list(books_collection.find({}, {'_id': 0}))
        if books:
            return jsonify(books)
        else:
            return 'Nothing found', 404

    if request.method == 'POST':
        new_book = {
            'author': request.form['author'],
            'language': request.form['language'],
            'title': request.form['title'],
            'id': books_collection.count_documents({}) + 1
        }
        books_collection.insert_one(new_book)
        return jsonify(new_book), 201

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    book = books_collection.find_one({'id': id}, {'_id': 0})
    if book is None:
        return 'Book not found', 404

    if request.method == 'GET':
        return jsonify(book)

    if request.method == 'PUT':
        update_data = {
            'author': request.form['author'],
            'language': request.form['language'],
            'title': request.form['title']
        }
        books_collection.update_one({'id': id}, {'$set': update_data})
        return jsonify(update_data), 200

    if request.method == 'DELETE':
        books_collection.delete_one({'id': id})
        return jsonify({'message': 'Book deleted'}), 200
