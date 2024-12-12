from flask import Flask, render_template, request, redirect
from models import db, Book  # Import the database and model

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    books = Book.query.all()  # Fetch all books from the database
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)