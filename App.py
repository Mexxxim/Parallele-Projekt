from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Bookshelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    genre = db.Column(db.String(50))


@app.route('')
def index():
    return render_template('index.html')

# gets all books from the bookshelf
@app.route('/Bookshelf', methods=['GET'])
def get_books():
    return Bookshelf

# gets a single book from the Bookshelf by its id and return an error if its not found
@app.route('/Bookshelf/<int:Book_id>', methods=['GET'])
def get_book(book_id):
    for book in Bookshelf:
        if book['id']==book_id:
            return book
        
    return{'error':'Book not in Shelf'}

# adds a new book to the Bookshelf
@app.route('/Bookshelf', methods=['POST'])
def create_book():
    new_book={'id':len(Bookshelf)+1, 'titel':request.json['titel'], 'author':request.json['author']}
    Bookshelf.append(new_book)
    return new_book

# updates the credentials of a book in the Bookshelf
@app.route('/Bookshelf/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in Bookshelf:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book
    return{'error':'Book not in Shelf'}

# removes a book from the Bookshelf
@app.route('/Bookshelf/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in Bookshelf:
        if book['id']==book_id:
            book.remove(book)
            return{"data:""Successfully removed Book from Bookshelf"}
        
    return{'error':'Book not in Shelf'}


# runs app in degub mode to show the full error
if __name__ == '__main__':
    app.run(debug=True)