class Person:
    def __init__(self, person_id, name, email):
        self.person_id = person_id
        self.name = name
        self.email = email

    def display_details(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        # Create a Person object
person1 = Person(101, "Liz", "liz@gmail.com")

# Display person details
person1.display_details()