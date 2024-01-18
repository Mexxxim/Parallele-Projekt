from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    genre = db.Column(db.String(50))


@app.route('/')
def index():
    return render_template('index.html')

#define the route for submits for GET and POST to get the information 
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        id= request.form['id']
        title= request.form['title']
        author= request.form['author']
        genre= request.form['genre']

        book=Book(id,title,author,genre)
        db.session.add(book)
        db.session.commit()

# gets all books from the bookshelf
@app.route('/Book', methods=['GET'])
def get_books():
    return Book

# gets a single book from the Bookshelf by its id and return an error if its not found
@app.route('/Book/<int:Book_id>', methods=['GET'])
def get_book(book_id):
    for book in Book:
        if book['id']==book_id:
            return book
        
    return{'error':'Book not in Shelf'}

# adds a new book to the Bookshelf
@app.route('/Book', methods=['POST'])
def create_book():
    new_book={'id':len(Book)+1, 'titel':request.json['titel'], 'author':request.json['author']}
    Book.append(new_book)
    return new_book

# updates the credentials of a book in the Bookshelf
@app.route('/Bookshelf/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in Book:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book
    return{'error':'Book not in Shelf'}

# removes a book from the Bookshelf
@app.route('/Book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in Book:
        if book['id']==book_id:
            book.remove(book)
            return{"data:""Successfully removed Book from Bookshelf"}
        
    return{'error':'Book not in Shelf'}


# runs app in degub mode to show the full error
if __name__ == '__main__':
    app.run(debug=True)