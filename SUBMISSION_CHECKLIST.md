# Submission Checklist for Home Library Management App

## Required Deliverables

### 1. ✅ Link to Public Git Repository

**Status**: Ready
**Action Required**:
1. Create a repository on GitHub/GitLab
2. Push your code:
   ```bash
   git remote add origin <your-repo-url>
   git branch -M main
   git push -u origin main
   ```
3. Make repository public
4. Copy the URL for submission

**Example**: `https://github.com/yourusername/library-management-app`

---

### 2. ✅ ZIP Archive with Main Branch

**Status**: Ready to create
**Action Required**:
```bash
# From project root directory
git archive --format=zip --output=../home-library-management.zip HEAD
```

Or manually:
1. Create ZIP of entire project folder
2. Ensure it includes:
   - app.py
   - models.py
   - requirements.txt
   - app/ folder (static, templates)
   - diagrams/ folder
   - docs/ folder
   - README.md
   - .env.example
   - .gitignore

**File**: `home-library-management.zip`

---

### 3. ✅ PDF File with Technical Documentation and Diagrams

**Status**: Ready to convert
**Action Required**:

#### Option A: Using Online Converter
1. Go to https://www.markdowntopdf.com/
2. Upload `docs/TECHNICAL_DOCUMENTATION.md`
3. Download PDF

#### Option B: Using VS Code Extension
1. Install "Markdown PDF" extension
2. Open `docs/TECHNICAL_DOCUMENTATION.md`
3. Right-click → "Markdown PDF: Export (pdf)"

#### Option C: Using pandoc
```bash
pandoc docs/TECHNICAL_DOCUMENTATION.md -o technical-documentation.pdf
```

#### For UML Diagrams:
Convert PlantUML files to images:

**Online Method**:
1. Go to http://www.plantuml.com/plantuml/uml/
2. For each .puml file in diagrams/:
   - Copy content
   - Paste in web editor
   - Download as PNG
3. Insert images into PDF

**Local Method** (if you have PlantUML installed):
```bash
plantuml diagrams/*.puml
# This creates PNG files for each diagram
```

Then create combined PDF:
```bash
# Combine technical doc + diagrams into one PDF
# Use Word/LibreOffice/Google Docs to merge
```

**File**: `technical-documentation.pdf`

---

### 4. ✅ PDF File with User Manual

**Status**: Ready to convert
**Action Required**:

Same methods as above, but for `docs/USER_MANUAL.md`

```bash
pandoc docs/USER_MANUAL.md -o user-manual.pdf
```

Or use online converter: https://www.markdowntopdf.com/

**File**: `user-manual.pdf`

---

## Final Files to Upload to Moodle

```
📁 Submission Files:
├── Link: https://github.com/yourusername/library-management-app
├── home-library-management.zip          (~50 KB)
├── technical-documentation.pdf          (with UML diagrams)
└── user-manual.pdf
```

---

## Pre-Submission Tests

### Functionality Tests

- [ ] Application starts without errors
  ```bash
  python app.py
  ```

- [ ] Database connection works
  - Check `.env` file exists with correct DATABASE_URL

- [ ] Can add a book
  - Open browser: http://localhost:5000
  - Click "Add Book"
  - Fill form and submit

- [ ] Can edit a book
  - Click "Edit" on any book
  - Modify fields
  - Save changes

- [ ] Can delete a book
  - Click "Delete" on any book
  - Confirm deletion

- [ ] Search works
  - Type in search box
  - Books filter correctly

- [ ] Status filter works
  - Select different statuses
  - Books filter correctly

- [ ] Statistics display correctly
  - Check dashboard numbers
  - Verify they match your data

- [ ] Export CSV works
  - Click "Export CSV"
  - File downloads

- [ ] Export JSON works
  - Click "Export JSON"
  - File downloads

### Code Quality Checks

- [ ] No syntax errors in Python files
  ```bash
  python -m py_compile app.py
  python -m py_compile models.py
  ```

- [ ] No console errors in browser
  - Open browser DevTools (F12)
  - Check Console tab for errors

- [ ] All files have proper encoding (UTF-8)

- [ ] Comments are clear and helpful

### Documentation Checks

- [ ] README.md is complete and accurate

- [ ] USER_MANUAL.md covers all features

- [ ] TECHNICAL_DOCUMENTATION.md is detailed

- [ ] All UML diagrams are present and valid

- [ ] No broken links in documentation

---

## Quick Commands Reference

### Create ZIP Archive
```bash
# Method 1: Git archive (recommended)
git archive --format=zip --output=../home-library-management.zip HEAD

# Method 2: Manual zip
cd ..
zip -r home-library-management.zip finalProject/ -x "*.git*" "*/venv/*" "*/__pycache__/*" "*.pyc"
```

### Convert Markdown to PDF
```bash
# Install pandoc (if not installed)
# Mac: brew install pandoc
# Windows: choco install pandoc
# Linux: sudo apt install pandoc

# Convert files
pandoc docs/TECHNICAL_DOCUMENTATION.md -o technical-documentation.pdf --pdf-engine=xelatex
pandoc docs/USER_MANUAL.md -o user-manual.pdf --pdf-engine=xelatex
```

### Generate UML Diagram Images
```bash
# Install PlantUML
# Mac: brew install plantuml
# Windows/Linux: Download from https://plantuml.com

# Generate images
cd diagrams
plantuml *.puml
# This creates PNG files
```

---

## Moodle Submission Steps

1. **Log into Moodle**
2. **Navigate to Course** → Final Project Assignment
3. **Upload Files**:
   - Paste repository link in text field
   - Attach `home-library-management.zip`
   - Attach `technical-documentation.pdf`
   - Attach `user-manual.pdf`
4. **Add Submission Comments** (optional):
   ```
   Home Library Management Application

   Technologies:
   - Python 3 + Flask + SQLAlchemy
   - PostgreSQL
   - HTML/CSS/JavaScript

   Features:
   - Complete CRUD operations for books
   - Reading progress tracking
   - Multi-entity relationships
   - Library statistics
   - Data export (CSV/JSON)

   All required deliverables included:
   - Source code (GitHub + ZIP)
   - Technical documentation with UML diagrams
   - User manual
   ```
5. **Submit Assignment**

---

## Contact Information (if needed)

**Student**: [Your Name]
**Group**: [Your Group Number]
**Date**: December 2024

---

## Post-Submission

After submission:
- [ ] Verify files were uploaded correctly
- [ ] Keep a local backup of all files
- [ ] Note the submission timestamp
- [ ] Save submission confirmation email/screenshot

---

## Troubleshooting

### "Can't create ZIP file"
- Use online ZIP creator
- Or manually compress folder in Finder/Explorer

### "PDF conversion not working"
- Use Google Docs: File → Download → PDF
- Or use online tool: https://www.markdowntopdf.com/

### "PlantUML diagrams not rendering"
- Use online PlantUML editor: http://www.plantuml.com/plantuml/
- Take screenshots and insert into PDF

### "Git repository too large"
- Make sure venv/ and __pycache__/ are in .gitignore
- Use `git status` to check what's being tracked

---

**Good luck with your submission! 🎓**
