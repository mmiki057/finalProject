from flask import Flask, render_template, request, jsonify, send_file
from models import db, Book, Author, Publisher, Series, Genre, Topic, Category
from sqlalchemy import func, or_
import os
from dotenv import load_dotenv
import csv
import json
import io
from datetime import datetime

load_dotenv()

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

database_url = os.getenv('DATABASE_URL', 'postgresql://localhost/library_db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-me')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/books', methods=['GET'])
def get_books():
    search = request.args.get('search', '')
    status = request.args.get('status', '')

    query = Book.query

    if search:
        query = query.filter(or_(
            Book.title.ilike(f'%{search}%'),
            Book.description.ilike(f'%{search}%')
        ))

    if status:
        query = query.filter(Book.reading_status == status)

    books = query.all()
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'isbn': b.isbn,
        'publication_year': b.publication_year,
        'pages': b.pages,
        'reading_status': b.reading_status,
        'current_page': b.current_page,
        'rating': b.rating,
        'publisher': {'id': b.publisher.id, 'name': b.publisher.name} if b.publisher else None,
        'authors': [{'id': a.id, 'name': f'{a.first_name} {a.last_name}'} for a in b.authors],
        'genres': [{'id': g.id, 'name': g.name} for g in b.genres],
        'series': {'id': b.series.id, 'name': b.series.name} if b.series else None,
        'category': {'id': b.category.id, 'name': b.category.name} if b.category else None
    } for b in books])


@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'title': book.title,
        'isbn': book.isbn,
        'publication_year': book.publication_year,
        'pages': book.pages,
        'language': book.language,
        'description': book.description,
        'reading_status': book.reading_status,
        'current_page': book.current_page,
        'notes': book.notes,
        'rating': book.rating,
        'date_started': book.date_started.isoformat() if book.date_started else None,
        'date_completed': book.date_completed.isoformat() if book.date_completed else None,
        'publisher_id': book.publisher_id,
        'series_id': book.series_id,
        'series_position': book.series_position,
        'category_id': book.category_id,
        'author_ids': [a.id for a in book.authors],
        'genre_ids': [g.id for g in book.genres],
        'topic_ids': [t.id for t in book.topics]
    })


@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.json
    book = Book(
        title=data['title'],
        isbn=data.get('isbn'),
        publication_year=data.get('publication_year'),
        pages=data.get('pages'),
        language=data.get('language'),
        description=data.get('description'),
        publisher_id=data['publisher_id'],
        series_id=data.get('series_id'),
        series_position=data.get('series_position'),
        category_id=data.get('category_id'),
        reading_status=data.get('reading_status', 'unread')
    )

    if 'author_ids' in data:
        book.authors = Author.query.filter(Author.id.in_(data['author_ids'])).all()
    if 'genre_ids' in data:
        book.genres = Genre.query.filter(Genre.id.in_(data['genre_ids'])).all()
    if 'topic_ids' in data:
        book.topics = Topic.query.filter(Topic.id.in_(data['topic_ids'])).all()

    db.session.add(book)
    db.session.commit()

    return jsonify({'id': book.id, 'message': 'Book created'}), 201


@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json

    for field in ['title', 'isbn', 'publication_year', 'pages', 'language',
                  'description', 'publisher_id', 'series_id', 'series_position',
                  'category_id', 'reading_status', 'current_page', 'notes', 'rating']:
        if field in data:
            setattr(book, field, data[field])

    if 'author_ids' in data:
        book.authors = Author.query.filter(Author.id.in_(data['author_ids'])).all()
    if 'genre_ids' in data:
        book.genres = Genre.query.filter(Genre.id.in_(data['genre_ids'])).all()
    if 'topic_ids' in data:
        book.topics = Topic.query.filter(Topic.id.in_(data['topic_ids'])).all()

    db.session.commit()
    return jsonify({'message': 'Book updated'})


@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204
@app.route('/api/authors', methods=['GET', 'POST'])
def authors():
    if request.method == 'GET':
        authors = Author.query.all()
        return jsonify([{'id': a.id, 'first_name': a.first_name, 'last_name': a.last_name, 'full_name': f'{a.first_name} {a.last_name}'} for a in authors])
    else:
        data = request.json
        author = Author(first_name=data['first_name'], last_name=data['last_name'], biography=data.get('biography'))
        db.session.add(author)
        db.session.commit()
        return jsonify({'id': author.id}), 201


@app.route('/api/authors/<int:id>', methods=['PUT', 'DELETE'])
def author(id):
    author = Author.query.get_or_404(id)
    if request.method == 'PUT':
        data = request.json
        author.first_name = data.get('first_name', author.first_name)
        author.last_name = data.get('last_name', author.last_name)
        author.biography = data.get('biography', author.biography)
        db.session.commit()
        return jsonify({'message': 'Author updated'})
    else:
        db.session.delete(author)
        db.session.commit()
        return '', 204
@app.route('/api/publishers', methods=['GET', 'POST'])
def publishers():
    if request.method == 'GET':
        pubs = Publisher.query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'country': p.country} for p in pubs])
    else:
        data = request.json
        pub = Publisher(name=data['name'], country=data.get('country'))
        db.session.add(pub)
        db.session.commit()
        return jsonify({'id': pub.id}), 201
@app.route('/api/genres', methods=['GET', 'POST'])
def genres():
    if request.method == 'GET':
        return jsonify([{'id': g.id, 'name': g.name} for g in Genre.query.all()])
    else:
        genre = Genre(name=request.json['name'], description=request.json.get('description'))
        db.session.add(genre)
        db.session.commit()
        return jsonify({'id': genre.id}), 201


@app.route('/api/topics', methods=['GET', 'POST'])
def topics():
    if request.method == 'GET':
        return jsonify([{'id': t.id, 'name': t.name} for t in Topic.query.all()])
    else:
        topic = Topic(name=request.json['name'], description=request.json.get('description'))
        db.session.add(topic)
        db.session.commit()
        return jsonify({'id': topic.id}), 201


@app.route('/api/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return jsonify([{'id': c.id, 'name': c.name} for c in Category.query.all()])
    else:
        category = Category(name=request.json['name'], description=request.json.get('description'))
        db.session.add(category)
        db.session.commit()
        return jsonify({'id': category.id}), 201


@app.route('/api/series', methods=['GET', 'POST'])
def series():
    if request.method == 'GET':
        return jsonify([{'id': s.id, 'name': s.name} for s in Series.query.all()])
    else:
        data = request.json
        ser = Series(name=data['name'], description=data.get('description'), total_books=data.get('total_books'))
        if 'author_ids' in data:
            ser.authors = Author.query.filter(Author.id.in_(data['author_ids'])).all()
        db.session.add(ser)
        db.session.commit()
        return jsonify({'id': ser.id}), 201
@app.route('/api/library/stats')
def library_stats():
    total_books = Book.query.count()
    status_stats = db.session.query(Book.reading_status, func.count(Book.id)).group_by(Book.reading_status).all()

    return jsonify({
        'total_books': total_books,
        'total_authors': Author.query.count(),
        'total_publishers': Publisher.query.count(),
        'reading_status': {status: count for status, count in status_stats},
        'recent_books': [{
            'id': b.id,
            'title': b.title,
            'authors': [f'{a.first_name} {a.last_name}' for a in b.authors]
        } for b in Book.query.order_by(Book.created_at.desc()).limit(5).all()]
    })
@app.route('/api/export/csv')
def export_csv():
    books = Book.query.all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Title', 'ISBN', 'Year', 'Pages', 'Authors', 'Publisher', 'Status', 'Rating'])

    for book in books:
        writer.writerow([
            book.id, book.title, book.isbn, book.publication_year, book.pages,
            ', '.join([f'{a.first_name} {a.last_name}' for a in book.authors]),
            book.publisher.name if book.publisher else '',
            book.reading_status, book.rating
        ])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'library_{datetime.now().strftime("%Y%m%d")}.csv'
    )


@app.route('/api/export/json')
def export_json():
    books = Book.query.all()
    data = {
        'export_date': datetime.now().isoformat(),
        'total': len(books),
        'books': [{
            'title': b.title,
            'isbn': b.isbn,
            'year': b.publication_year,
            'pages': b.pages,
            'authors': [f'{a.first_name} {a.last_name}' for a in b.authors],
            'publisher': b.publisher.name if b.publisher else None,
            'status': b.reading_status,
            'rating': b.rating
        } for b in books]
    }

    return send_file(
        io.BytesIO(json.dumps(data, indent=2).encode('utf-8')),
        mimetype='application/json',
        as_attachment=True,
        download_name=f'library_{datetime.now().strftime("%Y%m%d")}.json'
    )
@app.cli.command()
def init_db():
    db.create_all()
    print('Database initialized!')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
