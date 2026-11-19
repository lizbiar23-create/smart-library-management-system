
from services.book_service import BookService
from services.student_service import StudentService
from services.librarian_service import LibrarianService
from services.borrowing_service import BorrowingService
from database.library_db import connect_database

# Create service objects
book_service = BookService()
student_service = StudentService()
librarian_service = LibrarianService()
borrowing_service = BorrowingService()

def view_borrowing_records():

    connection = connect_database()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                borrow_records.record_id,
                students.name,
                books.title,
                borrow_records.borrow_date,
                borrow_records.due_date,
                borrow_records.return_date
            FROM borrow_records
            JOIN students
            ON borrow_records.student_id = students.student_id
            JOIN books
            ON borrow_records.book_id = books.book_id
        """)

        records = cursor.fetchall()

        if not records:
            print("\nNo borrowing records found.")
            return

        print("\n--- Borrowing Records ---")

        for record in records:
            print(f"\nRecord ID: {record[0]}")
            print(f"Student: {record[1]}")
            print(f"Book: {record[2]}")
            print(f"Borrow Date: {record[3]}")
            print(f"Due Date: {record[4]}")
            print(f"Return Date: {record[5] or 'Not returned'}")
            print("---------------------------")

    finally:
        connection.close()

def main():

    while True:

        print("\n====================================")
        print("   SMART LIBRARY MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Register Student")
        print("2. Register Librarian")
        print("3. Add New Book")
        print("4. View All Books")
        print("5. Search for a Book")
        print("6. Borrow a Book")
        print("7. Return a Book")
        print("8. View Borrowing Records")
        print("9. View Registered Students")
        print("10. View Registered Librarians")
        print("11. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":

                print("\n--- Register Student ---")

                student_id = int(input("Enter Student ID: "))
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                department = input("Enter Department: ")

                student_service.register_student(
                    student_id, name, email, department
                )

            elif choice == "2":

                print("\n--- Register Librarian ---")

                librarian_id = int(input("Enter Librarian ID: "))
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                employee_number = input("Enter Employee Number: ")

                librarian_service.register_librarian(
                    librarian_id, name, email, employee_number
                )

            elif choice == "3":

                print("\n--- Add New Book ---")

                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author: ")
                year = int(input("Enter Publication Year: "))

                book_service.add_book(
                    book_id, title, author, year
                )

            elif choice == "4":

                book_service.display_books()

            elif choice == "5":

                title = input("Enter book title to search: ")
                book_service.search_book(title)

            elif choice == "6":

                print("\n--- Borrow a Book ---")

                student_id = int(input("Enter Student ID: "))
                book_id = int(input("Enter Book ID: "))

                borrowing_service.borrow_book(
                    student_id, book_id
                )

            elif choice == "7":

                print("\n--- Return a Book ---")

                student_id = int(input("Enter Student ID: "))
                book_id = int(input("Enter Book ID: "))

                borrowing_service.return_book(
                    student_id, book_id
                )

            elif choice == "8":

                view_borrowing_records()

            elif choice == "9":

                student_service.display_students()

            elif choice == "10":

                librarian_service.display_librarians()

            elif choice == "11":

                print("\nThank you for using Smart Library!")
                break

            else:

                print("\nInvalid choice. Please select a valid option.")

        except ValueError:

            print("\nInvalid input. Please enter numbers where required.")

        except Exception as error:

            print(f"\nSomething went wrong: {error}")

if __name__ == "__main__":
    main()