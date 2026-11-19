class Book:
    def __init__(self, book_id, title, author, publication_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def display_info(self):
        print("\n--- Book Information ---")
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Available: {self.is_available}")

# Create a book object
book1 = Book(1, "Python Programming", "John Smith", 2024)

# Display book information
book1.display_info()