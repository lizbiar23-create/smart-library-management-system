
import sqlite3
from database.library_db import connect_database

class BookService:

    # Add a new book
    def add_book(self, book_id, title, author, publication_year):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO books
                (book_id, title, author, publication_year)
                VALUES (?, ?, ?, ?)
            """, (book_id, title, author, publication_year))

            connection.commit()

            print(f"Book '{title}' added successfully!")

        except sqlite3.IntegrityError:
            print("Error: This book ID already exists.")

        finally:
            connection.close()

    # Display all books
    def display_books(self):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()

            if not books:
                print("No books registered yet.")
                return

            print("\n--- Library Book Collection ---")

            for book in books:
                status = "Available" if book[4] == 1 else "Borrowed"

                print(f"Book ID: {book[0]}")
                print(f"Title: {book[1]}")
                print(f"Author: {book[2]}")
                print(f"Publication Year: {book[3]}")
                print(f"Status: {status}")
                print("-------------------------------")

        finally:
            connection.close()

    # Search for a book by title
    def search_book(self, title):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT * FROM books
                WHERE title LIKE ?
            """, (f"%{title}%",))

            results = cursor.fetchall()

            if not results:
                print("Book not found.")
                return

            print("\n--- Search Results ---")

            for book in results:
                print(f"Book ID: {book[0]}")
                print(f"Title: {book[1]}")
                print(f"Author: {book[2]}")
                print(f"Publication Year: {book[3]}")

        finally:
            connection.close()

# Testing the Book Service
if __name__ == "__main__":

    service = BookService()

    service.add_book(
        1,
        "Python Programming",
        "John Smith",
        2024
    )

    service.display_books()

    service.search_book("Python")