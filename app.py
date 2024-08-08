from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "author":"guy 0",
        "language": "english",
        "title": "title 0",
    },
    {
        "id": 1,
        "author":"guy 1",
        "language": "english",
        "title": "title 1",
    },
    {
        "id": 2,
        "author":"guy 2",
        "language": "german",
        "title": "title 2",
    },
    {
        "id": 3,
        "author":"guy 3",
        "language": "english",
        "title": "title 3",
    }
]

@app.route('/books', methods = ['GET','POST'])

def books():
    if request.method == 'GET':    
        if len(books_list) > 0 :
            return jsonify(books_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_author = request.form('author')
        new_lang =  request.form('language')
        new_title = request.form('title')
        iD = books_list[-1]['id']+1

        new_obj = {
            'id':iD,
            'author':new_author,
            'language':new_lang,
            'title':new_title
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/book/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form('author')
                book['language'] =  request.form('language')
                book['title'] = request.form('title')
                updated_book = {

                'id':id,
                'author':book['author'],
                'language':book['language'],
                'title':book['title']
            }
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)

if __name__ == "__main__":
    app.run(debug= True)