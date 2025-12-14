// Global state
let books = [];
let authors = [];
let publishers = [];
let genres = [];
let topics = [];
let categories = [];
let series = [];

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    loadStats();
    loadBooks();
    loadAuthors();
    loadPublishers();
    loadGenres();
    loadTopics();
    loadCategories();
    loadSeries();
    loadRecommendations();
});

// Load library statistics
async function loadStats() {
    try {
        const response = await fetch('/api/library/stats');
        const data = await response.json();

        document.getElementById('totalBooks').textContent = data.total_books;
        document.getElementById('totalAuthors').textContent = data.total_authors;
        document.getElementById('readingBooks').textContent = data.reading_status.reading || 0;
        document.getElementById('completedBooks').textContent = data.reading_status.completed || 0;
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

// Load books
async function loadBooks() {
    const search = document.getElementById('searchInput').value;
    const status = document.getElementById('statusFilter').value;

    try {
        const response = await fetch(`/api/books?search=${search}&status=${status}`);
        books = await response.json();
        renderBooks();
    } catch (error) {
        console.error('Error loading books:', error);
    }
}

// Render books grid
function renderBooks() {
    const grid = document.getElementById('booksGrid');

    if (books.length === 0) {
        grid.innerHTML = '<p style="text-align:center; padding:40px;">No books found. Add your first book!</p>';
        return;
    }

    grid.innerHTML = books.map(book => `
        <div class="book-card">
            <h3>${book.title}</h3>
            <p class="book-meta">
                ${book.authors.map(a => a.name).join(', ') || 'Unknown Author'}
            </p>
            <p class="book-meta">
                ${book.publisher ? book.publisher.name : 'Unknown Publisher'}
            </p>
            ${book.publication_year ? `<p class="book-meta">Year: ${book.publication_year}</p>` : ''}
            ${book.pages ? `<p class="book-meta">Pages: ${book.pages}</p>` : ''}
            ${book.rating ? `<p class="book-meta">⭐ ${book.rating}/5</p>` : ''}
            <span class="book-status status-${book.reading_status}">
                ${book.reading_status.toUpperCase()}
            </span>
            ${book.reading_status === 'reading' && book.current_page && book.pages ?
                `<p class="book-meta">Progress: ${book.current_page}/${book.pages} (${Math.round(book.current_page/book.pages*100)}%)</p>` : ''}
            <div class="book-actions">
                <button onclick="editBook(${book.id})" class="btn-primary">Edit</button>
                <button onclick="deleteBook(${book.id})" class="btn-danger">Delete</button>
            </div>
        </div>
    `).join('');
}

// Load reference data
async function loadAuthors() {
    const response = await fetch('/api/authors');
    authors = await response.json();
    populateSelect('bookAuthors', authors, 'full_name');
}

async function loadPublishers() {
    const response = await fetch('/api/publishers');
    publishers = await response.json();
    populateSelect('bookPublisher', publishers, 'name', true);
}

async function loadGenres() {
    const response = await fetch('/api/genres');
    genres = await response.json();
    populateSelect('bookGenres', genres, 'name');
}

async function loadTopics() {
    const response = await fetch('/api/topics');
    topics = await response.json();
}

async function loadCategories() {
    const response = await fetch('/api/categories');
    categories = await response.json();
    populateSelect('bookCategory', categories, 'name');
}

async function loadSeries() {
    const response = await fetch('/api/series');
    series = await response.json();
    populateSelect('bookSeries', series, 'name');
}

// Populate select dropdown
function populateSelect(selectId, data, labelField, includeEmpty = false) {
    const select = document.getElementById(selectId);
    select.innerHTML = includeEmpty ? '<option value="">Select...</option>' : '';

    data.forEach(item => {
        const option = document.createElement('option');
        option.value = item.id;
        option.textContent = item[labelField];
        select.appendChild(option);
    });
}

// Show add book form
function showAddBookForm() {
    document.getElementById('modalTitle').textContent = 'Add Book';
    document.getElementById('bookForm').reset();
    document.getElementById('bookId').value = '';
    document.getElementById('bookModal').style.display = 'block';
}

// Edit book
async function editBook(id) {
    try {
        const response = await fetch(`/api/books/${id}`);
        const book = await response.json();

        document.getElementById('modalTitle').textContent = 'Edit Book';
        document.getElementById('bookId').value = book.id;
        document.getElementById('bookTitle').value = book.title;
        document.getElementById('bookIsbn').value = book.isbn || '';
        document.getElementById('bookYear').value = book.publication_year || '';
        document.getElementById('bookPages').value = book.pages || '';
        document.getElementById('bookLanguage').value = book.language || '';
        document.getElementById('bookDescription').value = book.description || '';
        document.getElementById('bookPublisher').value = book.publisher_id;
        document.getElementById('bookSeries').value = book.series_id || '';
        document.getElementById('bookCategory').value = book.category_id || '';
        document.getElementById('bookStatus').value = book.reading_status;
        document.getElementById('bookCurrentPage').value = book.current_page || 0;
        document.getElementById('bookRating').value = book.rating || '';
        document.getElementById('bookNotes').value = book.notes || '';

        // Set multiple select values
        setMultipleSelect('bookAuthors', book.author_ids);
        setMultipleSelect('bookGenres', book.genre_ids);

        document.getElementById('bookModal').style.display = 'block';
    } catch (error) {
        console.error('Error loading book:', error);
    }
}

// Set multiple select values
function setMultipleSelect(selectId, values) {
    const select = document.getElementById(selectId);
    Array.from(select.options).forEach(option => {
        option.selected = values.includes(parseInt(option.value));
    });
}

// Save book (create or update)
async function saveBook(event) {
    event.preventDefault();

    const id = document.getElementById('bookId').value;
    const data = {
        title: document.getElementById('bookTitle').value,
        isbn: document.getElementById('bookIsbn').value || null,
        publication_year: document.getElementById('bookYear').value || null,
        pages: document.getElementById('bookPages').value || null,
        language: document.getElementById('bookLanguage').value || null,
        description: document.getElementById('bookDescription').value || null,
        publisher_id: parseInt(document.getElementById('bookPublisher').value),
        series_id: document.getElementById('bookSeries').value || null,
        category_id: document.getElementById('bookCategory').value || null,
        reading_status: document.getElementById('bookStatus').value,
        current_page: document.getElementById('bookCurrentPage').value || 0,
        rating: document.getElementById('bookRating').value || null,
        notes: document.getElementById('bookNotes').value || null,
        author_ids: Array.from(document.getElementById('bookAuthors').selectedOptions).map(o => parseInt(o.value)),
        genre_ids: Array.from(document.getElementById('bookGenres').selectedOptions).map(o => parseInt(o.value))
    };

    try {
        const url = id ? `/api/books/${id}` : '/api/books';
        const method = id ? 'PUT' : 'POST';

        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            closeModal();
            loadBooks();
            loadStats();
            alert(id ? 'Book updated successfully!' : 'Book added successfully!');
        }
    } catch (error) {
        console.error('Error saving book:', error);
        alert('Error saving book');
    }
}

// Delete book
async function deleteBook(id) {
    if (!confirm('Are you sure you want to delete this book?')) return;

    try {
        const response = await fetch(`/api/books/${id}`, { method: 'DELETE' });
        if (response.ok) {
            loadBooks();
            loadStats();
            alert('Book deleted successfully!');
        }
    } catch (error) {
        console.error('Error deleting book:', error);
    }
}

// Close modal
function closeModal() {
    document.getElementById('bookModal').style.display = 'none';
}

// Quick add author or publisher
function showQuickAdd(type) {
    const name = prompt(`Enter ${type} name:`);
    if (!name) return;

    if (type === 'author') {
        const parts = name.split(' ');
        const firstName = parts[0];
        const lastName = parts.slice(1).join(' ') || parts[0];

        fetch('/api/authors', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ first_name: firstName, last_name: lastName })
        }).then(() => loadAuthors());
    } else if (type === 'publisher') {
        fetch('/api/publishers', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: name })
        }).then(() => loadPublishers());
    }
}

// Export data
function exportData(format) {
    window.location.href = `/api/export/${format}`;
}

// Close modal on outside click
window.onclick = function(event) {
    const modal = document.getElementById('bookModal');
    if (event.target === modal) {
        closeModal();
    }
}

// Load recommendations
async function loadRecommendations() {
    try {
        const response = await fetch('/api/recommendations');
        const data = await response.json();

        const section = document.getElementById('recommendationsSection');
        const intro = document.getElementById('recommendationsIntro');
        const grid = document.getElementById('recommendationsGrid');

        // Show recommendations section if we have data
        if (data.recommendations && data.recommendations.length > 0) {
            section.style.display = 'block';

            // Update intro text
            const stats = data.user_reading_stats;
            if (stats.completed_books > 0 && stats.favorite_genres.length > 0) {
                intro.textContent = `Based on your ${stats.completed_books} completed book(s) in ${stats.favorite_genres.join(', ')}, here are some recommendations:`;
            } else {
                intro.textContent = 'Here are some top-rated books to get you started:';
            }

            // Render recommendations
            grid.innerHTML = data.recommendations.map(rec => `
                <div class="recommendation-card">
                    <h3>${rec.title}</h3>
                    <p class="recommendation-author">by ${rec.author}</p>
                    <div class="recommendation-info">
                        <span class="recommendation-year">${rec.publication_year || 'N/A'}</span>
                        <span class="recommendation-pages">${rec.pages || 'N/A'} pages</span>
                    </div>
                    <div class="recommendation-genres">
                        ${rec.genres.map(g => `<span class="genre-tag">${g.name}</span>`).join('')}
                    </div>
                    <p class="recommendation-description">${rec.description || ''}</p>
                </div>
            `).join('');
        } else {
            section.style.display = 'none';
        }
    } catch (error) {
        console.error('Error loading recommendations:', error);
    }
}
