import sqlite3
from database.library_db import connect_database


class LibrarianService:

    def register_librarian(self, librarian_id, name, email, employee_number):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO librarians
                (librarian_id, name, email, employee_number)
                VALUES (?, ?, ?, ?)
            """, (librarian_id, name, email, employee_number))

            connection.commit()

            print(f"Librarian {name} registered successfully!")

        except sqlite3.IntegrityError:
            print("Error: Librarian ID, email or employee number already exists.")

        finally:
            connection.close()

    def display_librarians(self):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM librarians")

            librarians = cursor.fetchall()

            if not librarians:
                print("No librarians registered yet.")
                return

            print("\n--- Registered Librarians ---")

            for librarian in librarians:
                print(f"Librarian ID: {librarian[0]}")
                print(f"Name: {librarian[1]}")
                print(f"Email: {librarian[2]}")
                print(f"Employee Number: {librarian[3]}")
                print("-----------------------------")

        finally:
            connection.close()


# Testing the Librarian Service
if __name__ == "__main__":

    service = LibrarianService()

    service.register_librarian(
        201,
        "John",
        "john@gmail.com",
        "LIB001"
    )

    service.display_librarians()