# Smart Library Management System

**Student Name:** Deng Agok Biar Kuiorot Deng  
**Student ID:** 2517289  
**Course:** Advanced Python Programming

## 1. Project Overview

The Smart Library Management System is a Python-based application designed to manage the daily activities of a library.

The system allows librarians to manage books, register students, manage librarian information, and keep track of borrowed and returned books.

It uses Python object-oriented programming (OOP) and an SQLite database to store and manage information.

## 2. Technologies Used

- Python
- SQLite Database
- Visual Studio Code
- Git and GitHub

## 3. Main Features

1. **Student Registration:** Register students with their ID, name, email, and department.
2. **Librarian Registration:** Register librarians and store their employee information.
3. **Book Management:** Add new books and view the library collection.
4. **Book Search:** Search for books by title.
5. **Borrow Books:** Allow registered students to borrow available books.
6. **Return Books:** Record returned books and update their availability.
7. **Borrowing Records:** View borrowing history, due dates, and return dates.
8. **Database Management:** Store information using an SQLite database.

## 4. Project Structure

```text
smart-library-management-system/
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── person.py
│   ├── student.py
│   └── librarian.py
│
├── database/
│   ├── __init__.py
│   ├── library_db.py
│   └── library.db
│
├── services/
│   ├── __init__.py
│   ├── book_service.py
│   ├── student_service.py
│   ├── librarian_service.py
│   └── borrowing_service.py
│
├── tests/
│
├── .vscode/
│   ├── settings.json
│   └── launch.json
│
├── main.py
└── README.md
```

## 5. How to Run the Project

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal in the project folder.
4. Run the application using:

```bash
python main.py
```

5. Follow the menu instructions to use the system.

## 6. Database

The project uses SQLite to store:

- Student information
- Librarian information
- Book information
- Borrowing records

The database also tracks book availability and borrowing and return dates.

## 7. Conclusion

The Smart Library Management System demonstrates the practical use of Python programming, object-oriented programming, database management, and modular software development.

The project provides a simple way to organize library activities and manage borrowing and returning operations.