import sqlite3
from pathlib import Path


# Database file location
DB_PATH = Path(__file__).resolve().parent / "library.db"


def connect_database():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():

    connection = connect_database()

    cursor = connection.cursor()

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL
        )
    """)

    # Librarians table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS librarians (
            librarian_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            employee_number TEXT UNIQUE NOT NULL
        )
    """)

    # Books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            is_available INTEGER DEFAULT 1
        )
    """)

    # Borrowing records table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrow_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            borrow_date TEXT NOT NULL,
            due_date TEXT NOT NULL,
            return_date TEXT,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")
    print("All four tables are ready.")


# Test database creation
if __name__ == "__main__":
    create_tables()