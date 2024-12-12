from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(4), nullable=False)