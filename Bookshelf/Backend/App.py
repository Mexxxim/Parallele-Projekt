from flask import render_template, request, Flask
from flask_sqlalchemy import SQLAlchemy

#connection to the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#creates a table with there columns in the database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    genre = db.Column(db.String(50))

    def __repr__(self):
        return f"Book: {self.titel}"
    
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        

def format_Books(event):
    return {
        "id": event.id,
        "title": event.title,
        "author": event.author,
        "genre": event.genre
    }
   
@app.route('/')
def index():
    return render_template('index.html')

#create a book
@app.route('/events', methods=['POST'])
def create_event():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']
    event = Book(title, author, genre)
    db.session.add(event)
    db.session.commit()
    return format_Books(event)

#get all books
@app.route('/events', methods = ['GET'])
def get_events():
    events = Book.query.order_by(Book.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_Books(event))
    return {'events': event_list}

#get a single book
@app.route('/events/<id>', methods = ['GET'])
def get_event(id):
    event = Book.query.filter_by(id=id).one()
    formatted_Books = format_Books(event)
    return {'event': formatted_Books}

#delete a Book
@app.route('/events/<id>', methods = ['DELETE'])
def delete_book(id):
    event = Book.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Book (id: {id}) removed from Shelf'

#Edit a Book
@app.route('/events/<id>', methods = ['PUT'])
def update_book(id):
    event = Book.query.filter_by(id=id)
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']
    event.update(dict(title = title, author = author, genre = genre))
    db.session.commit()
    return {'event': format_Books(event.one())}

# runs app in degub mode to show the full error
if __name__ == '__main__':
    app.run(debug=True)