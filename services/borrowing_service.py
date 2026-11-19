
import sqlite3
from datetime import date, timedelta
from database.library_db import connect_database

class BorrowingService:

    # Borrow a book
    def borrow_book(self, student_id, book_id):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            # Check whether the student exists
            cursor.execute(
                "SELECT * FROM students WHERE student_id = ?",
                (student_id,)
            )
            student = cursor.fetchone()

            if not student:
                print("Error: Student not found.")
                return

            # Check whether the book exists and is available
            cursor.execute(
                "SELECT * FROM books WHERE book_id = ?",
                (book_id,)
            )
            book = cursor.fetchone()

            if not book:
                print("Error: Book not found.")
                return

            if book[4] == 0:
                print("Sorry, this book is already borrowed.")
                return

            # Set borrowing and due dates
            borrow_date = date.today()
            due_date = borrow_date + timedelta(days=14)

            # Update book availability
            cursor.execute(
                "UPDATE books SET is_available = 0 WHERE book_id = ?",
                (book_id,)
            )

            # Save the borrowing record
            cursor.execute("""
                INSERT INTO borrow_records
                (student_id, book_id, borrow_date, due_date)
                VALUES (?, ?, ?, ?)
            """, (
                student_id,
                book_id,
                borrow_date.isoformat(),
                due_date.isoformat()
            ))

            connection.commit()

            print(f"Book '{book[1]}' borrowed successfully!")
            print(f"Borrow Date: {borrow_date}")
            print(f"Due Date: {due_date}")

        finally:
            connection.close()

    # Return a book
    def return_book(self, student_id, book_id):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            # Find an active borrowing record
            cursor.execute("""
                SELECT record_id FROM borrow_records
                WHERE student_id = ?
                AND book_id = ?
                AND return_date IS NULL
            """, (student_id, book_id))

            record = cursor.fetchone()

            if not record:
                print("No active borrowing record found.")
                return

            # Record the return date
            return_date = date.today()

            cursor.execute("""
                UPDATE borrow_records
                SET return_date = ?
                WHERE record_id = ?
            """, (return_date.isoformat(), record[0]))

            # Make the book available again
            cursor.execute("""
                UPDATE books
                SET is_available = 1
                WHERE book_id = ?
            """, (book_id,))

            connection.commit()

            print("Book returned successfully!")
            print(f"Return Date: {return_date}")

        finally:
            connection.close()

# Test the Borrowing Service
if __name__ == "__main__":

    service = BorrowingService()

    service.borrow_book(101, 1)

    # To test returning, comment out the borrow line above
    # and remove the # from the line below.
    # service.return_book(101, 1)