# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.8+
- PostgreSQL

### Setup

1. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure database**
   ```bash
   cp .env.example .env
   # Edit .env with your PostgreSQL credentials
   ```

3. **Initialize with sample data**
   ```bash
   python init_sample_data.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open browser**
   ```
   http://localhost:5000
   ```

## 📚 What You'll See

The app will start with 5 sample books including:
- 1984 by George Orwell
- Pride and Prejudice by Jane Austen
- Harry Potter by J.K. Rowling
- And more...

## ✨ Try These Features

1. **Add a Book**: Click "+ Add Book" button
2. **Search**: Type in the search box
3. **Filter**: Use status dropdown (Unread/Reading/Completed)
4. **Edit**: Click "Edit" on any book card
5. **Export**: Click "Export CSV" or "Export JSON"

## 📖 Documentation

- **User Manual**: `docs/USER_MANUAL.md`
- **Technical Docs**: `docs/TECHNICAL_DOCUMENTATION.md`
- **Project Summary**: `PROJECT_SUMMARY.md`
- **Submission Guide**: `SUBMISSION_CHECKLIST.md`

## 🎯 For Submission

See `SUBMISSION_CHECKLIST.md` for complete submission instructions.

## 🆘 Troubleshooting

**Can't connect to database?**
- Check PostgreSQL is running
- Verify `.env` DATABASE_URL is correct
- Create database: `createdb library_db`

**Port 5000 already in use?**
- Change port in `app.py`: `app.run(debug=True, port=5001)`

**Dependencies won't install?**
- Upgrade pip: `pip install --upgrade pip`
- Try: `pip install -r requirements.txt --no-cache-dir`

---

**Need help?** Check the full documentation in the `docs/` folder.
