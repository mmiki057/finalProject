Home Library Management App

Web application for managing your personal book collection.

Features

Book Management: Add, edit, delete, search and filter books
Reading Progress Tracking: Track reading status, current page, ratings and notes
Organization: Categorize by genres, topics, categories, and series
Multi-entity Support: Books, Authors, Publishers, Series, Genres, Topics, Categories
Statistics Dashboard: View library overview and reading statistics
Data Export: Export library to CSV or JSON format

Technologies

Backend: Python 3 + Flask + SQLAlchemy
Database: PostgreSQL
Frontend: HTML + CSS + Vanilla JavaScript

Setup and Run

 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate     Windows: venv\Scripts\activate
pip install -r requirements.txt
```

 2. Configure Database

Create `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost:5432/library_db
SECRET_KEY=your-secret-key
```

Or copy from example:
```bash
cp .env.example .env
 Then edit .env with your credentials
```

 3. Initialize Database with Sample Data

```bash
python init_sample_data.py
```

Database Schema

The application implements these relationships:

Each book has exactly one publisher
Each book can have many authors (0 or more)
Each book can belong to one series (optional)
Each book can have many genres (0 or more)
Each book can have many topics (0 or more)
Each book can belong to one category (optional)
Each series can have many authors (1 or more)

Quick Start Commands

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
createdb library_db
cp .env.example .env
python init_sample_data.py
python app.py
```

Open browser: http://localhost:5000

