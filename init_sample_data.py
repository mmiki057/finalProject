"""
Initialize database with sample data for testing
Run this after setting up the database to populate with example books
"""

from app import app
from models import db, Book, Author, Publisher, Series, Genre, Topic, Category

def init_sample_data():
    """Initialize database with sample data"""

    with app.app_context():
        # Clear existing data (optional - comment out if you want to keep existing data)
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()

        print("Creating sample data...")

        # Create Publishers
        penguin = Publisher(name="Penguin Random House", country="USA")
        harpercollins = Publisher(name="HarperCollins", country="USA")
        oxford = Publisher(name="Oxford University Press", country="UK")

        db.session.add_all([penguin, harpercollins, oxford])
        db.session.commit()

        # Create Authors
        author1 = Author(first_name="George", last_name="Orwell",
                        biography="English novelist and essayist")
        author2 = Author(first_name="Jane", last_name="Austen",
                        biography="English novelist")
        author3 = Author(first_name="J.K.", last_name="Rowling",
                        biography="British author")
        author4 = Author(first_name="Stephen", last_name="King",
                        biography="American author of horror fiction")

        db.session.add_all([author1, author2, author3, author4])
        db.session.commit()

        # Create Genres
        fiction = Genre(name="Fiction", description="Literary fiction")
        fantasy = Genre(name="Fantasy", description="Fantasy literature")
        horror = Genre(name="Horror", description="Horror fiction")
        classic = Genre(name="Classic", description="Classic literature")
        romance = Genre(name="Romance", description="Romantic fiction")

        db.session.add_all([fiction, fantasy, horror, classic, romance])
        db.session.commit()

        # Create Categories
        favorites = Category(name="Favorites", description="My favorite books")
        to_read = Category(name="To Read", description="Books to read")
        reference = Category(name="Reference", description="Reference books")

        db.session.add_all([favorites, to_read, reference])
        db.session.commit()

        # Create Topics
        politics = Topic(name="Politics", description="Political themes")
        society = Topic(name="Society", description="Social commentary")
        magic = Topic(name="Magic", description="Magical elements")

        db.session.add_all([politics, society, magic])
        db.session.commit()

        # Create Series
        hp_series = Series(name="Harry Potter", description="Fantasy series about a young wizard",
                          total_books=7)
        hp_series.authors.append(author3)

        db.session.add(hp_series)
        db.session.commit()

        # Create Books
        book1 = Book(
            title="1984",
            isbn="9780451524935",
            publication_year=1949,
            pages=328,
            language="English",
            description="A dystopian social science fiction novel",
            reading_status="completed",
            current_page=328,
            rating=5.0,
            publisher=penguin,
            category=favorites
        )
        book1.authors.append(author1)
        book1.genres.extend([fiction, classic])
        book1.topics.extend([politics, society])

        book2 = Book(
            title="Pride and Prejudice",
            isbn="9780141439518",
            publication_year=1813,
            pages=432,
            language="English",
            description="A romantic novel of manners",
            reading_status="completed",
            rating=4.5,
            publisher=penguin,
            category=favorites
        )
        book2.authors.append(author2)
        book2.genres.extend([fiction, classic, romance])

        book3 = Book(
            title="Harry Potter and the Philosopher's Stone",
            isbn="9780747532699",
            publication_year=1997,
            pages=223,
            language="English",
            description="The first book in the Harry Potter series",
            reading_status="reading",
            current_page=150,
            rating=4.8,
            publisher=harpercollins,
            series=hp_series,
            series_position=1,
            category=to_read
        )
        book3.authors.append(author3)
        book3.genres.extend([fiction, fantasy])
        book3.topics.append(magic)

        book4 = Book(
            title="The Shining",
            isbn="9780307743657",
            publication_year=1977,
            pages=447,
            language="English",
            description="A horror novel about a family in an isolated hotel",
            reading_status="unread",
            publisher=penguin,
            category=to_read
        )
        book4.authors.append(author4)
        book4.genres.extend([fiction, horror])

        book5 = Book(
            title="Animal Farm",
            isbn="9780451526342",
            publication_year=1945,
            pages=112,
            language="English",
            description="Allegorical novella about Stalinism",
            reading_status="completed",
            current_page=112,
            rating=4.7,
            publisher=penguin,
            category=favorites
        )
        book5.authors.append(author1)
        book5.genres.extend([fiction, classic])
        book5.topics.extend([politics, society])

        db.session.add_all([book1, book2, book3, book4, book5])
        db.session.commit()

        print("\n✅ Sample data created successfully!")
        print(f"\nCreated:")
        print(f"  - {Publisher.query.count()} publishers")
        print(f"  - {Author.query.count()} authors")
        print(f"  - {Book.query.count()} books")
        print(f"  - {Genre.query.count()} genres")
        print(f"  - {Category.query.count()} categories")
        print(f"  - {Topic.query.count()} topics")
        print(f"  - {Series.query.count()} series")
        print("\nYou can now run the application: python app.py")

if __name__ == "__main__":
    init_sample_data()
