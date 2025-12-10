# Home Library Management App

A simple web application for managing your personal book collection.

## Features

- **Book Management**: Add, edit, delete, search and filter books
- **Reading Progress Tracking**: Track reading status, current page, ratings and notes
- **Organization**: Categorize by genres, topics, categories, and series
- **Multi-entity Support**: Books, Authors, Publishers, Series, Genres, Topics, Categories
- **Statistics Dashboard**: View library overview and reading statistics
- **Data Export**: Export library to CSV or JSON format

## Technologies

- **Backend**: Python 3 + Flask + SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: HTML + CSS + Vanilla JavaScript

## Setup and Run

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Database

Create `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost:5432/library_db
SECRET_KEY=your-secret-key
```

Or copy from example:
```bash
cp .env.example .env
# Then edit .env with your credentials
```

### 3. Initialize Database with Sample Data

```bash
python init_sample_data.py
```

This creates example books, authors, publishers, etc.

### 4. Run Application

```bash
python app.py
```

### 5. Open Browser

Navigate to: **http://localhost:5000**

## Project Structure

```
├── app.py                  # Main Flask application
├── models.py               # Database models
├── init_sample_data.py     # Sample data loader
├── requirements.txt        # Python dependencies
├── app/
│   ├── static/            # CSS and JavaScript
│   └── templates/         # HTML templates
└── diagrams/              # UML diagrams
```

## Database Schema

The application implements these relationships:

- Each book has **exactly one publisher**
- Each book can have **many authors** (0 or more)
- Each book can belong to **one series** (optional)
- Each book can have **many genres** (0 or more)
- Each book can have **many topics** (0 or more)
- Each book can belong to **one category** (optional)
- Each series can have **many authors** (1 or more)

## API Endpoints

### Books
- `GET /api/books` - Get all books (with search and filter)
- `GET /api/books/{id}` - Get single book
- `POST /api/books` - Create book
- `PUT /api/books/{id}` - Update book
- `DELETE /api/books/{id}` - Delete book

### Other Entities
- `GET/POST /api/authors` - Manage authors
- `GET/POST /api/publishers` - Manage publishers
- `GET/POST /api/genres` - Manage genres
- `GET/POST /api/topics` - Manage topics
- `GET/POST /api/categories` - Manage categories
- `GET/POST /api/series` - Manage series

### Library
- `GET /api/library/stats` - Get statistics
- `GET /api/export/csv` - Export to CSV
- `GET /api/export/json` - Export to JSON

## UML Diagrams

UML diagrams are located in the `diagrams/` folder in PlantUML format:

- **use_case_diagram.puml** - User interactions with the system
- **class_diagram.puml** - Database entities and relationships
- **activity_diagram.puml** - Workflow for adding a book
- **sequence_diagram.puml** - Reading progress update flow

To view diagrams, use:
- Online: http://www.plantuml.com/plantuml/
- VS Code: Install PlantUML extension

## Development

### Run without sample data

```bash
python app.py
```

The database tables will be created automatically on first run.

### Check syntax

```bash
python -m py_compile app.py models.py
```

## Troubleshooting

**Database connection error?**
- Check PostgreSQL is running
- Verify `.env` file has correct DATABASE_URL
- Create database: `createdb library_db`

**Port 5000 in use?**
- Change port in app.py: `app.run(debug=True, port=5001)`

**Can't install dependencies?**
- Update pip: `pip install --upgrade pip`

## License

Educational project for Object-Oriented Programming course at UEK.
