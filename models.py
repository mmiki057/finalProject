from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

book_authors = db.Table('book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)

book_genres = db.Table('book_genres',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

book_topics = db.Table('book_topics',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('topic_id', db.Integer, db.ForeignKey('topics.id'), primary_key=True)
)

series_authors = db.Table('series_authors',
    db.Column('series_id', db.Integer, db.ForeignKey('series.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)

recommended_book_genres = db.Table('recommended_book_genres',
    db.Column('recommended_book_id', db.Integer, db.ForeignKey('recommended_books.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.Text)

    def __repr__(self):
        return f'<Author {self.first_name} {self.last_name}>'


class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    country = db.Column(db.String(100))
    books = db.relationship('Book', backref='publisher', lazy=True)

    def __repr__(self):
        return f'<Publisher {self.name}>'


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Genre {self.name}>'


class Topic(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Topic {self.name}>'


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    books = db.relationship('Book', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'


class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    total_books = db.Column(db.Integer)
    books = db.relationship('Book', backref='series', lazy=True)
    authors = db.relationship('Author', secondary=series_authors, backref='series')

    def __repr__(self):
        return f'<Series {self.name}>'


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(300), nullable=False)
    isbn = db.Column(db.String(13))
    publication_year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    language = db.Column(db.String(50))
    description = db.Column(db.Text)

    reading_status = db.Column(db.String(20), default='unread')  # unread, reading, completed
    current_page = db.Column(db.Integer, default=0)
    notes = db.Column(db.Text)
    rating = db.Column(db.Float)
    date_started = db.Column(db.Date)
    date_completed = db.Column(db.Date)

    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
    series_position = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    authors = db.relationship('Author', secondary=book_authors, backref='books')
    genres = db.relationship('Genre', secondary=book_genres, backref='books')
    topics = db.relationship('Topic', secondary=book_topics, backref='books')

    def __repr__(self):
        return f'<Book {self.title}>'


class RecommendedBook(db.Model):
    __tablename__ = 'recommended_books'
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(300), nullable=False)
    author_name = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(13))
    publication_year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    language = db.Column(db.String(50), default='English')
    description = db.Column(db.Text)
    average_rating = db.Column(db.Float)

    genres = db.relationship('Genre', secondary=recommended_book_genres, backref='recommended_books')

    def __repr__(self):
        return f'<RecommendedBook {self.title}>'
