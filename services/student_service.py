import sqlite3
from database.library_db import connect_database


class StudentService:

    def register_student(self, student_id, name, email, department):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO students
                (student_id, name, email, department)
                VALUES (?, ?, ?, ?)
            """, (student_id, name, email, department))

            connection.commit()

            print(f"Student {name} registered successfully!")

        except sqlite3.IntegrityError:
            print("Error: Student ID or email already exists.")

        finally:
            connection.close()

    def display_students(self):

        connection = connect_database()

        try:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM students")

            students = cursor.fetchall()

            if not students:
                print("No students registered yet.")
                return

            print("\n--- Registered Students ---")

            for student in students:
                print(f"Student ID: {student[0]}")
                print(f"Name: {student[1]}")
                print(f"Email: {student[2]}")
                print(f"Department: {student[3]}")
                print("---------------------------")

        finally:
            connection.close()


# Testing the Student Service
if __name__ == "__main__":

    service = StudentService()

    service.register_student(
        101,
        "Liz",
        "liz@gmail.com",
        "Smart Computing"
    )

    service.display_students()