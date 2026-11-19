from person import Person


class Librarian(Person):

    def __init__(self, librarian_id, name, email, employee_number):
        super().__init__(librarian_id, name, email)

        self.employee_number = employee_number
        self.role = "Librarian"

    def add_book(self, book):
        print(f"Librarian {self.name} added '{book.title}' to the library.")

    def remove_book(self, book):
        print(f"Librarian {self.name} removed '{book.title}' from the library.")

    def display_details(self):
        print("\n--- Librarian Information ---")
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Employee Number: {self.employee_number}")
        print(f"Role: {self.role}")


# Testing the Librarian class
if __name__ == "__main__":

    librarian1 = Librarian(
        201,
        "John",
        "john@gmail.com",
        "LIB001"
    )

    librarian1.display_details()