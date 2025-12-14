from app import app
from models import db, Book, Author, Publisher, Series, Genre, Topic, Category, RecommendedBook

def init_sample_data():
    with app.app_context():
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()

        print("Creating sample data...")
        penguin = Publisher(name="Penguin Random House", country="USA")
        harpercollins = Publisher(name="HarperCollins", country="USA")
        oxford = Publisher(name="Oxford University Press", country="UK")

        db.session.add_all([penguin, harpercollins, oxford])
        db.session.commit()
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
        fiction = Genre(name="Fiction", description="Literary fiction")
        fantasy = Genre(name="Fantasy", description="Fantasy literature")
        horror = Genre(name="Horror", description="Horror fiction")
        classic = Genre(name="Classic", description="Classic literature")
        romance = Genre(name="Romance", description="Romantic fiction")

        db.session.add_all([fiction, fantasy, horror, classic, romance])
        db.session.commit()
        favorites = Category(name="Favorites", description="My favorite books")
        to_read = Category(name="To Read", description="Books to read")
        reference = Category(name="Reference", description="Reference books")

        db.session.add_all([favorites, to_read, reference])
        db.session.commit()
        politics = Topic(name="Politics", description="Political themes")
        society = Topic(name="Society", description="Social commentary")
        magic = Topic(name="Magic", description="Magical elements")

        db.session.add_all([politics, society, magic])
        db.session.commit()
        hp_series = Series(name="Harry Potter", description="Fantasy series about a young wizard",
                          total_books=7)
        hp_series.authors.append(author3)

        db.session.add(hp_series)
        db.session.commit()
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

        print("Creating recommended books catalog...")

        recommended_books_data = [
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180, 4.0, ["Fiction", "Classic"]),
            ("To Kill a Mockingbird", "Harper Lee", 1960, 324, 4.3, ["Fiction", "Classic"]),
            ("The Catcher in the Rye", "J.D. Salinger", 1951, 277, 3.8, ["Fiction", "Classic"]),
            ("Brave New World", "Aldous Huxley", 1932, 311, 3.9, ["Fiction", "Classic"]),
            ("The Road", "Cormac McCarthy", 2006, 287, 4.0, ["Fiction"]),
            ("Life of Pi", "Yann Martel", 2001, 460, 3.9, ["Fiction"]),
            ("The Book Thief", "Markus Zusak", 2005, 552, 4.4, ["Fiction"]),
            ("The Kite Runner", "Khaled Hosseini", 2003, 371, 4.3, ["Fiction"]),
            ("The Alchemist", "Paulo Coelho", 1988, 208, 3.9, ["Fiction"]),
            ("One Hundred Years of Solitude", "Gabriel García Márquez", 1967, 417, 4.1, ["Fiction", "Classic"]),
            ("The Count of Monte Cristo", "Alexandre Dumas", 1844, 1276, 4.3, ["Fiction", "Classic"]),
            ("War and Peace", "Leo Tolstoy", 1869, 1225, 4.1, ["Fiction", "Classic"]),
            ("Anna Karenina", "Leo Tolstoy", 1877, 864, 4.0, ["Fiction", "Classic"]),
            ("The Brothers Karamazov", "Fyodor Dostoevsky", 1880, 824, 4.3, ["Fiction", "Classic"]),
            ("Crime and Punishment", "Fyodor Dostoevsky", 1866, 671, 4.2, ["Fiction", "Classic"]),
            ("Wuthering Heights", "Emily Brontë", 1847, 416, 3.9, ["Fiction", "Classic", "Romance"]),
            ("Jane Eyre", "Charlotte Brontë", 1847, 532, 4.1, ["Fiction", "Classic", "Romance"]),
            ("The Picture of Dorian Gray", "Oscar Wilde", 1890, 254, 4.1, ["Fiction", "Classic"]),
            ("Moby-Dick", "Herman Melville", 1851, 585, 3.5, ["Fiction", "Classic"]),
            ("The Adventures of Huckleberry Finn", "Mark Twain", 1884, 366, 3.8, ["Fiction", "Classic"]),

            # Fantasy (20 books)
            ("The Lord of the Rings", "J.R.R. Tolkien", 1954, 1178, 4.5, ["Fantasy", "Fiction"]),
            ("The Hobbit", "J.R.R. Tolkien", 1937, 310, 4.3, ["Fantasy", "Fiction"]),
            ("A Game of Thrones", "George R.R. Martin", 1996, 694, 4.4, ["Fantasy", "Fiction"]),
            ("The Name of the Wind", "Patrick Rothfuss", 2007, 662, 4.5, ["Fantasy", "Fiction"]),
            ("The Way of Kings", "Brandon Sanderson", 2010, 1007, 4.6, ["Fantasy", "Fiction"]),
            ("Mistborn: The Final Empire", "Brandon Sanderson", 2006, 541, 4.4, ["Fantasy", "Fiction"]),
            ("The Eye of the World", "Robert Jordan", 1990, 782, 4.2, ["Fantasy", "Fiction"]),
            ("The Chronicles of Narnia", "C.S. Lewis", 1950, 767, 4.2, ["Fantasy", "Fiction"]),
            ("American Gods", "Neil Gaiman", 2001, 465, 4.1, ["Fantasy", "Fiction"]),
            ("Good Omens", "Terry Pratchett & Neil Gaiman", 1990, 383, 4.3, ["Fantasy", "Fiction"]),
            ("The Colour of Magic", "Terry Pratchett", 1983, 206, 3.9, ["Fantasy", "Fiction"]),
            ("Jonathan Strange & Mr Norrell", "Susanna Clarke", 2004, 782, 3.8, ["Fantasy", "Fiction"]),
            ("The Lies of Locke Lamora", "Scott Lynch", 2006, 499, 4.3, ["Fantasy", "Fiction"]),
            ("Gardens of the Moon", "Steven Erikson", 1999, 666, 3.8, ["Fantasy", "Fiction"]),
            ("The Blade Itself", "Joe Abercrombie", 2006, 515, 4.2, ["Fantasy", "Fiction"]),
            ("The Fifth Season", "N.K. Jemisin", 2015, 512, 4.3, ["Fantasy", "Fiction"]),
            ("Assassin's Apprentice", "Robin Hobb", 1995, 435, 4.1, ["Fantasy", "Fiction"]),
            ("The Bear and the Nightingale", "Katherine Arden", 2017, 322, 4.0, ["Fantasy", "Fiction"]),
            ("Elantris", "Brandon Sanderson", 2005, 638, 4.0, ["Fantasy", "Fiction"]),
            ("Warbreaker", "Brandon Sanderson", 2009, 592, 4.2, ["Fantasy", "Fiction"]),

            # Horror (15 books)
            ("It", "Stephen King", 1986, 1138, 4.2, ["Horror", "Fiction"]),
            ("The Stand", "Stephen King", 1978, 1153, 4.3, ["Horror", "Fiction"]),
            ("Carrie", "Stephen King", 1974, 199, 3.9, ["Horror", "Fiction"]),
            ("Pet Sematary", "Stephen King", 1983, 374, 4.0, ["Horror", "Fiction"]),
            ("Misery", "Stephen King", 1987, 320, 4.2, ["Horror", "Fiction"]),
            ("Dracula", "Bram Stoker", 1897, 418, 4.0, ["Horror", "Classic"]),
            ("Frankenstein", "Mary Shelley", 1818, 280, 3.8, ["Horror", "Classic"]),
            ("The Haunting of Hill House", "Shirley Jackson", 1959, 246, 3.9, ["Horror", "Fiction"]),
            ("Bird Box", "Josh Malerman", 2014, 262, 3.8, ["Horror", "Fiction"]),
            ("The Exorcist", "William Peter Blatty", 1971, 385, 4.0, ["Horror", "Fiction"]),
            ("House of Leaves", "Mark Z. Danielewski", 2000, 709, 4.1, ["Horror", "Fiction"]),
            ("The Silence of the Lambs", "Thomas Harris", 1988, 338, 4.2, ["Horror", "Fiction"]),
            ("Interview with the Vampire", "Anne Rice", 1976, 371, 3.9, ["Horror", "Fiction"]),
            ("Ghost Story", "Peter Straub", 1979, 567, 3.8, ["Horror", "Fiction"]),
            ("The Hellbound Heart", "Clive Barker", 1986, 164, 3.8, ["Horror", "Fiction"]),

            # Romance (15 books)
            ("Outlander", "Diana Gabaldon", 1991, 850, 4.2, ["Romance", "Fiction"]),
            ("The Notebook", "Nicholas Sparks", 1996, 214, 4.1, ["Romance", "Fiction"]),
            ("Me Before You", "Jojo Moyes", 2012, 369, 4.3, ["Romance", "Fiction"]),
            ("The Time Traveler's Wife", "Audrey Niffenegger", 2003, 546, 3.9, ["Romance", "Fiction"]),
            ("Sense and Sensibility", "Jane Austen", 1811, 409, 4.1, ["Romance", "Classic"]),
            ("Emma", "Jane Austen", 1815, 474, 4.0, ["Romance", "Classic"]),
            ("Persuasion", "Jane Austen", 1817, 249, 4.1, ["Romance", "Classic"]),
            ("The Fault in Our Stars", "John Green", 2012, 313, 4.2, ["Romance", "Fiction"]),
            ("Eleanor & Park", "Rainbow Rowell", 2013, 328, 3.9, ["Romance", "Fiction"]),
            ("Attachments", "Rainbow Rowell", 2011, 323, 3.9, ["Romance", "Fiction"]),
            ("The Rosie Project", "Graeme Simsion", 2013, 295, 4.0, ["Romance", "Fiction"]),
            ("Red, White & Royal Blue", "Casey McQuiston", 2019, 421, 4.2, ["Romance", "Fiction"]),
            ("Beach Read", "Emily Henry", 2020, 361, 3.9, ["Romance", "Fiction"]),
            ("People We Meet on Vacation", "Emily Henry", 2021, 364, 4.0, ["Romance", "Fiction"]),
            ("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", 2017, 388, 4.4, ["Romance", "Fiction"]),

            # Classic (15 books)
            ("Don Quixote", "Miguel de Cervantes", 1605, 1023, 3.9, ["Classic", "Fiction"]),
            ("Ulysses", "James Joyce", 1922, 732, 3.7, ["Classic", "Fiction"]),
            ("The Odyssey", "Homer", -800, 541, 3.8, ["Classic"]),
            ("The Iliad", "Homer", -762, 683, 3.9, ["Classic"]),
            ("The Divine Comedy", "Dante Alighieri", 1320, 798, 4.0, ["Classic"]),
            ("Les Misérables", "Victor Hugo", 1862, 1463, 4.2, ["Classic", "Fiction"]),
            ("The Three Musketeers", "Alexandre Dumas", 1844, 700, 4.1, ["Classic", "Fiction"]),
            ("Madame Bovary", "Gustave Flaubert", 1856, 327, 3.6, ["Classic", "Fiction"]),
            ("The Scarlet Letter", "Nathaniel Hawthorne", 1850, 279, 3.4, ["Classic", "Fiction"]),
            ("Heart of Darkness", "Joseph Conrad", 1899, 96, 3.4, ["Classic", "Fiction"]),
            ("A Tale of Two Cities", "Charles Dickens", 1859, 448, 3.8, ["Classic", "Fiction"]),
            ("Great Expectations", "Charles Dickens", 1861, 505, 3.8, ["Classic", "Fiction"]),
            ("Oliver Twist", "Charles Dickens", 1838, 608, 3.9, ["Classic", "Fiction"]),
            ("The Canterbury Tales", "Geoffrey Chaucer", 1400, 504, 3.5, ["Classic"]),
            ("Gulliver's Travels", "Jonathan Swift", 1726, 306, 3.6, ["Classic", "Fiction"]),
        ]

        for title, author, year, pages, rating, genre_names in recommended_books_data:
            rec_book = RecommendedBook(
                title=title,
                author_name=author,
                publication_year=year,
                pages=pages,
                average_rating=rating,
                description=f"A recommended {', '.join(genre_names).lower()} book."
            )

            for genre_name in genre_names:
                genre = Genre.query.filter_by(name=genre_name).first()
                if genre:
                    rec_book.genres.append(genre)

            db.session.add(rec_book)

        db.session.commit()

        print("\nSample data created successfully!")
        print(f"\nCreated:")
        print(f"  - {Publisher.query.count()} publishers")
        print(f"  - {Author.query.count()} authors")
        print(f"  - {Book.query.count()} books")
        print(f"  - {Genre.query.count()} genres")
        print(f"  - {Category.query.count()} categories")
        print(f"  - {Topic.query.count()} topics")
        print(f"  - {Series.query.count()} series")
        print(f"  - {RecommendedBook.query.count()} recommended books")
        print("\nYou can now run the application: python app.py")

if __name__ == "__main__":
    init_sample_data()
