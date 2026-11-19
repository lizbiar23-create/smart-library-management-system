from person import Person


class Student(Person):

    def __init__(self, student_id, name, email, department):
        super().__init__(student_id, name, email)
        self.department = department
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{book.title} borrowed successfully.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{book.title} returned successfully.")
        else:
            print("This book was not borrowed by this student.")

    def display_details(self):
        print("\n--- Student Information ---")
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print(f"Borrowed Books: {len(self.borrowed_books)}")


# Test Student class
if __name__ == "__main__":

    student1 = Student(
        101,
        "Liz",
        "liz@gmail.com",
        "Smart Computing"
    )

    student1.display_details()
    
    