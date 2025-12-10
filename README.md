# Home Library Management App

A simple web application for managing your personal book collection.

## Technologies

- **Backend**: Python + Flask + SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: HTML + CSS + Vanilla JavaScript

## Project Structure

```
finalProject/
├── app.py              # Main application file
├── models.py           # Database models
├── requirements.txt    # Python dependencies
├── app/
│   ├── static/        # CSS, JS files
│   └── templates/     # HTML templates
├── diagrams/          # UML diagrams
└── docs/              # Documentation
```

## Installation and Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure PostgreSQL database and create `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost:5432/library_db
SECRET_KEY=your-secret-key
```

4. Initialize database:
```bash
python app.py
```

The database will be created automatically on first run.

5. (Optional) Load sample data for testing:
```bash
python init_sample_data.py
```

This will create example books, authors, publishers, etc.

6. Run the application:
```bash
python app.py
```

7. Open browser: http://localhost:5000

## Features

- Book management (add, edit, delete, search)
- Reading progress tracking
- Organization by categories, genres, authors, series
- Library statistics dashboard
- Data export/import (CSV, JSON)

## Business Rules

- Each book can have many authors (0 or more)
- Each author can write many books (at least 1)
- Each publisher can publish many books (at least 1)
- Each book is published by exactly one publisher
- Each series can have many books (at least 1)
- Each book belongs to at most one series
- Each series can be written by many authors (at least 1)
- Each author can have many book series
- Each book can represent many genres (0 or more)
- Each genre can have many books (0 or more)
- Each book can have many topics (0 or more)
- Each topic can have many books (0 or more)
- Each book can belong to one category
- Each category can have many books (0 or more)
