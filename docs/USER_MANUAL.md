# Home Library Management App - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Dashboard](#dashboard)
4. [Managing Books](#managing-books)
5. [Managing Authors and Publishers](#managing-authors-and-publishers)
6. [Reading Progress Tracking](#reading-progress-tracking)
7. [Organization Features](#organization-features)
8. [Data Export and Import](#data-export-and-import)
9. [Troubleshooting](#troubleshooting)

## Introduction

The Home Library Management App is a web-based application designed to help you organize and track your personal book collection. With this app, you can:

- Catalog your books with detailed information
- Track your reading progress
- Organize books by genres, categories, and series
- View statistics about your library
- Export and import your data

## Getting Started

### System Requirements
- Python 3.8 or higher
- PostgreSQL database
- Modern web browser (Chrome, Firefox, Safari, or Edge)

### Installation

1. Extract the application files to a directory on your computer
2. Open a terminal/command prompt in the application directory
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Create a `.env` file with your database configuration:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/library_db
   SECRET_KEY=your-secret-key
   ```
7. Run the application:
   ```bash
   python app.py
   ```
8. Open your web browser and navigate to: `http://localhost:5000`

## Dashboard

When you open the application, you'll see the main dashboard with:

### Statistics Cards
- **Total Books**: Shows the total number of books in your library
- **Currently Reading**: Number of books you're currently reading
- **Completed**: Number of books you've finished reading
- **Authors**: Total number of authors in your library

### Recent Books
The dashboard also displays your most recently added books.

## Managing Books

### Adding a New Book

1. Click the **"+ Add Book"** button in the top right corner
2. Fill in the book details:
   - **Title*** (required): The book's title
   - **ISBN**: International Standard Book Number
   - **Publication Year**: Year the book was published
   - **Pages**: Number of pages
   - **Language**: Book's language
   - **Description**: Brief summary or description
   - **Publisher*** (required): Select from dropdown or add new
   - **Authors**: Select one or more authors (or add new)
   - **Genres**: Select applicable genres
   - **Series**: If part of a series, select it
   - **Category**: Assign a category
   - **Reading Status**: Choose from Unread, Reading, or Completed
   - **Current Page**: Your current reading position
   - **Rating**: Rate the book from 0 to 5 stars
   - **Notes**: Personal notes about the book

3. Click **"Save"** to add the book to your library

### Editing a Book

1. Find the book in your library
2. Click the **"Edit"** button on the book card
3. Modify the desired fields
4. Click **"Save"** to update

### Deleting a Book

1. Find the book in your library
2. Click the **"Delete"** button on the book card
3. Confirm the deletion when prompted

⚠️ **Warning**: Deleting a book is permanent and cannot be undone!

### Searching and Filtering

- **Search Bar**: Type in the search box to find books by title or description
- **Status Filter**: Use the dropdown to filter books by reading status:
  - All Status
  - Unread
  - Reading
  - Completed

## Managing Authors and Publishers

### Adding an Author

When adding or editing a book:
1. Click **"+ Add Author"** below the Authors dropdown
2. Enter the author's full name (first name and last name)
3. The author will be immediately available in the dropdown

### Adding a Publisher

When adding or editing a book:
1. Click **"+ Add Publisher"** below the Publisher dropdown
2. Enter the publisher's name
3. The publisher will be immediately available in the dropdown

## Reading Progress Tracking

The app helps you track your reading progress for each book:

### Setting Reading Status

Books can have one of three statuses:
- **Unread**: Haven't started the book yet
- **Reading**: Currently reading
- **Completed**: Finished reading

### Tracking Current Page

For books you're reading:
1. Edit the book
2. Update the **Current Page** field
3. The app will automatically calculate your reading progress percentage

### Rating Books

After finishing a book:
1. Edit the book
2. Set the **Rating** field (0-5 stars)
3. Your rating will be displayed on the book card

### Adding Notes

Keep track of your thoughts:
1. Edit the book
2. Enter your notes in the **Notes** field
3. Use this for quotes, reflections, or reminders

## Organization Features

### Genres

Genres help classify books by their literary type (Fiction, Non-fiction, Mystery, Romance, etc.). A book can have multiple genres.

### Categories

Categories provide broad classification for your books (Personal shelves like "To Read", "Favorites", "Reference", etc.). Each book can belong to one category.

### Series

If your books are part of a series:
1. The app tracks series information
2. You can see all books in a series together
3. Series must have at least one author

### Topics

Topics are thematic tags for your books, allowing flexible organization beyond traditional genres.

## Data Export and Import

### Exporting Your Library

You can export your library data in two formats:

#### CSV Export
1. Click **"Export CSV"** in the header
2. A CSV file will be downloaded with all your book data
3. This format is great for spreadsheets and data analysis

#### JSON Export
1. Click **"Export JSON"** in the header
2. A JSON file will be downloaded with complete book data
3. This format preserves all relationships and is ideal for backups

### Importing Data

*Note: Import functionality is available through the API. See Technical Documentation for details.*

## Troubleshooting

### Application won't start
- Verify Python is installed: `python --version`
- Check that PostgreSQL is running
- Verify database credentials in `.env` file
- Check if port 5000 is available

### Can't add a book
- Ensure you've selected a publisher (required field)
- Check that the title is not empty
- Verify your database connection

### Books not displaying
- Try refreshing the page (F5 or Cmd+R)
- Check browser console for errors (F12)
- Verify database is accessible

### Search not working
- Clear the search box and try again
- Check your internet connection
- Refresh the page

## Tips and Best Practices

1. **Regular Backups**: Export your library regularly to keep backups
2. **Consistent Data Entry**: Use consistent formatting for author names and publishers
3. **Use Genres and Categories**: Properly categorize books for easier searching
4. **Update Progress Regularly**: Keep your reading progress current
5. **Add Notes**: Write notes while reading for better recall later

## Support

For technical issues or questions:
- Check the Technical Documentation
- Review the project's README.md file
- Submit issues to the project repository

---

*Last updated: December 2024*
