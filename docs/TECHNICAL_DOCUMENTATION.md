# Home Library Management App - Technical Documentation

## Table of Contents
1. [System Architecture](#system-architecture)
2. [Database Design](#database-design)
3. [Backend Implementation](#backend-implementation)
4. [Frontend Implementation](#frontend-implementation)
5. [API Documentation](#api-documentation)
6. [UML Diagrams](#uml-diagrams)
7. [Deployment](#deployment)

## System Architecture

### Overview

The Home Library Management App follows a three-tier architecture:

```
┌─────────────────────────────────────────┐
│         Presentation Layer              │
│    (HTML + CSS + Vanilla JavaScript)    │
└────────────────┬────────────────────────┘
                 │ HTTP/JSON
┌────────────────▼────────────────────────┐
│         Application Layer               │
│      (Flask + SQLAlchemy ORM)          │
└────────────────┬────────────────────────┘
                 │ SQL
┌────────────────▼────────────────────────┐
│           Data Layer                    │
│          (PostgreSQL)                   │
└─────────────────────────────────────────┘
```

### Technology Stack

- **Backend Framework**: Flask 3.0.0
- **ORM**: SQLAlchemy 3.1.1
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (ES6+)
- **HTTP Protocol**: RESTful API design

### Design Patterns Used

1. **MVC Pattern**: Separation of concerns between models, views, and controllers
2. **Repository Pattern**: Database access abstraction through SQLAlchemy ORM
3. **RESTful API**: Standardized HTTP methods for resource manipulation

## Database Design

### Entity-Relationship Model

The database implements the following business rules:

- Each book has **exactly one publisher**
- Each book can have **many authors** (0..*)
- Each book can belong to **at most one series** (0..1)
- Each book can have **many genres** (0..*)
- Each book can have **many topics** (0..*)
- Each book can belong to **one category** (0..1)
- Each series can have **many authors** (1..*)

### Database Schema

#### Core Tables

**books**
- `id` (PK): Integer
- `title`: String(300), NOT NULL
- `isbn`: String(13), UNIQUE
- `publication_year`: Integer
- `pages`: Integer
- `language`: String(50)
- `description`: Text
- `reading_status`: String(20), DEFAULT 'unread'
- `current_page`: Integer, DEFAULT 0
- `notes`: Text
- `rating`: Float
- `date_started`: Date
- `date_completed`: Date
- `publisher_id` (FK): Integer, NOT NULL → publishers.id
- `series_id` (FK): Integer → series.id
- `series_position`: Integer
- `category_id` (FK): Integer → categories.id
- `created_at`: DateTime, DEFAULT CURRENT_TIMESTAMP

**authors**
- `id` (PK): Integer
- `first_name`: String(100), NOT NULL
- `last_name`: String(100), NOT NULL
- `biography`: Text

**publishers**
- `id` (PK): Integer
- `name`: String(200), NOT NULL, UNIQUE
- `country`: String(100)

**series**
- `id` (PK): Integer
- `name`: String(200), NOT NULL
- `description`: Text
- `total_books`: Integer

**genres**
- `id` (PK): Integer
- `name`: String(100), NOT NULL, UNIQUE
- `description`: Text

**topics**
- `id` (PK): Integer
- `name`: String(100), NOT NULL, UNIQUE
- `description`: Text

**categories**
- `id` (PK): Integer
- `name`: String(100), NOT NULL, UNIQUE
- `description`: Text

#### Association Tables (Many-to-Many)

**book_authors**
- `book_id` (PK, FK): Integer → books.id
- `author_id` (PK, FK): Integer → authors.id

**book_genres**
- `book_id` (PK, FK): Integer → books.id
- `genre_id` (PK, FK): Integer → genres.id

**book_topics**
- `book_id` (PK, FK): Integer → books.id
- `topic_id` (PK, FK): Integer → topics.id

**series_authors**
- `series_id` (PK, FK): Integer → series.id
- `author_id` (PK, FK): Integer → authors.id

### Database Indexes

Primary indexes are automatically created on:
- All primary keys
- Foreign key relationships

Recommended additional indexes for performance:
- `books.title` (for search queries)
- `books.reading_status` (for filtering)
- `authors.last_name` (for sorting)

## Backend Implementation

### File Structure

```
app.py              # Main Flask application
models.py           # SQLAlchemy ORM models
app/
  ├── static/       # Static files
  │   ├── style.css
  │   └── app.js
  └── templates/    # HTML templates
      └── index.html
```

### Models (models.py)

#### Book Model

```python
class Book(db.Model):
    __tablename__ = 'books'

    # Relationships
    authors = db.relationship('Author', secondary=book_authors, backref='books')
    genres = db.relationship('Genre', secondary=book_genres, backref='books')
    topics = db.relationship('Topic', secondary=book_topics, backref='books')
    publisher = db.relationship('Publisher', backref='books')
    series = db.relationship('Series', backref='books')
    category = db.relationship('Category', backref='books')
```

Key Features:
- Implements many-to-many relationships using association tables
- Provides `__repr__` method for debugging
- Uses SQLAlchemy ORM for database operations

### Application Routes (app.py)

The application implements RESTful API endpoints following standard HTTP methods:

- **GET**: Retrieve resources
- **POST**: Create new resources
- **PUT**: Update existing resources
- **DELETE**: Remove resources

### Error Handling

- `404 Not Found`: Resource doesn't exist
- `400 Bad Request`: Invalid data submitted
- `201 Created`: Resource successfully created
- `204 No Content`: Resource successfully deleted

## Frontend Implementation

### Technology Choices

- **No Framework**: Uses Vanilla JavaScript for simplicity
- **Modern ES6+**: Arrow functions, async/await, template literals
- **Fetch API**: For HTTP requests
- **CSS Grid/Flexbox**: For responsive layout

### JavaScript Architecture (app.js)

#### Global State Management
```javascript
let books = [];
let authors = [];
let publishers = [];
// ... other reference data
```

#### Key Functions

1. **Data Loading**: `loadBooks()`, `loadAuthors()`, etc.
2. **Rendering**: `renderBooks()`
3. **CRUD Operations**: `saveBook()`, `editBook()`, `deleteBook()`
4. **UI Control**: `showAddBookForm()`, `closeModal()`

### CSS Design (style.css)

- **Responsive Grid**: Adapts to different screen sizes
- **Card-based Layout**: Books displayed as cards
- **Modal Dialog**: For add/edit operations
- **Status Indicators**: Color-coded reading status badges

## API Documentation

### Books API

#### GET /api/books
Retrieve all books with optional filtering

**Query Parameters:**
- `search` (optional): Search in title and description
- `status` (optional): Filter by reading status

**Response:**
```json
[
  {
    "id": 1,
    "title": "Book Title",
    "isbn": "9781234567890",
    "publication_year": 2023,
    "pages": 350,
    "reading_status": "reading",
    "current_page": 100,
    "rating": 4.5,
    "publisher": {"id": 1, "name": "Publisher Name"},
    "authors": [{"id": 1, "name": "Author Name"}],
    "genres": [{"id": 1, "name": "Fiction"}],
    "series": {"id": 1, "name": "Series Name"},
    "category": {"id": 1, "name": "Category Name"}
  }
]
```

#### GET /api/books/{id}
Retrieve a single book

**Response:**
```json
{
  "id": 1,
  "title": "Book Title",
  "isbn": "9781234567890",
  ...
  "author_ids": [1, 2],
  "genre_ids": [1],
  "topic_ids": [1, 2, 3]
}
```

#### POST /api/books
Create a new book

**Request Body:**
```json
{
  "title": "New Book",
  "isbn": "9781234567890",
  "publication_year": 2023,
  "pages": 300,
  "publisher_id": 1,
  "author_ids": [1, 2],
  "genre_ids": [1],
  "reading_status": "unread"
}
```

**Response:** `201 Created`

#### PUT /api/books/{id}
Update an existing book

**Request Body:** Same as POST

**Response:** `200 OK`

#### DELETE /api/books/{id}
Delete a book

**Response:** `204 No Content`

### Authors API

#### GET /api/authors
Retrieve all authors

#### POST /api/authors
Create a new author

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "biography": "Author biography"
}
```

### Publishers API

#### GET /api/publishers
Retrieve all publishers

#### POST /api/publishers
Create a new publisher

**Request Body:**
```json
{
  "name": "Publisher Name",
  "country": "USA"
}
```

### Library Statistics API

#### GET /api/library/stats
Retrieve library statistics

**Response:**
```json
{
  "total_books": 150,
  "total_authors": 75,
  "total_publishers": 30,
  "reading_status": {
    "unread": 50,
    "reading": 10,
    "completed": 90
  },
  "recent_books": [...]
}
```

### Export API

#### GET /api/export/csv
Export library data as CSV file

**Response:** CSV file download

#### GET /api/export/json
Export library data as JSON file

**Response:** JSON file download

## UML Diagrams

### Use Case Diagram
Located in `/diagrams/use_case_diagram.puml`

Shows user interactions with the system:
- Manage Books
- Track Reading Progress
- Manage Authors/Publishers
- Organize Books
- View Statistics
- Export/Import Data

### Class Diagram
Located in `/diagrams/class_diagram.puml`

Shows the object-oriented structure:
- Core classes: Book, Author, Publisher, Series, Genre, Topic, Category
- Relationships and multiplicities
- Attributes and methods

### Activity Diagram
Located in `/diagrams/activity_diagram.puml`

Shows the workflow for adding a new book:
- Form display
- Data entry
- Validation
- Database persistence
- UI update

### Sequence Diagram
Located in `/diagrams/sequence_diagram.puml`

Shows the interaction flow for updating reading progress:
- User → Browser → Flask → Database
- Request/response cycle
- Transaction handling

## Deployment

### Development Setup

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Configure database
5. Run application

### Production Considerations

1. **Database**: Use PostgreSQL in production
2. **Web Server**: Deploy with Gunicorn + Nginx
3. **Security**:
   - Use strong SECRET_KEY
   - Enable HTTPS
   - Implement authentication (optional enhancement)
4. **Environment Variables**: Store sensitive data in `.env`
5. **Backup**: Regular database backups

### Environment Variables

```
DATABASE_URL=postgresql://user:pass@host:port/dbname
SECRET_KEY=strong-random-key
FLASK_ENV=production
```

## Code Quality and Best Practices

### Python Code Standards
- Follows PEP 8 style guidelines
- Type hints where applicable
- Docstrings for functions and classes

### JavaScript Standards
- ES6+ syntax
- Async/await for asynchronous operations
- Consistent naming conventions

### Database Best Practices
- Foreign key constraints enforced
- CASCADE rules for data integrity
- Indexes on frequently queried columns

## Testing Recommendations

### Unit Tests
- Test model methods
- Test API endpoints
- Test data validation

### Integration Tests
- Test complete workflows
- Test database transactions
- Test API integration

### Manual Testing Checklist
- [ ] Add a book
- [ ] Edit a book
- [ ] Delete a book
- [ ] Search and filter
- [ ] Update reading progress
- [ ] Export data
- [ ] Verify statistics

## Future Enhancements

1. **User Authentication**: Multi-user support with login system
2. **Book Recommendations**: Algorithm-based suggestions
3. **Reading Goals**: Set and track yearly reading goals
4. **Book Cover Images**: Upload and display cover images
5. **Social Features**: Share reviews and reading lists
6. **Mobile App**: Native iOS/Android applications
7. **API Rate Limiting**: Prevent abuse
8. **Full-text Search**: Advanced search capabilities
9. **Import from External APIs**: Integration with Google Books API, Open Library
10. **Reading Analytics**: Detailed reading statistics and charts

---

*Last updated: December 2024*
