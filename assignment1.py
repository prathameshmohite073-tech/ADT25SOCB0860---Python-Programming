# Library Management System using OOP

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print(title, "added successfully.")

    # Register a new patron
    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(name, "registered successfully.")

    # Borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed successfully.")
                return
        print("Book is not available.")

    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully.")
                return
        print("Book not found.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            if book.available:
                print(book.title, "- Available")
            else:
                print(book.title, "- Borrowed")


# Main Program
library = Library()

library.add_book("Python Basics")
library.add_book("Data Structures")

library.register_patron("Purva")

library.display_books()

library.borrow_book("Python Basics")

library.display_books()

library.return_book("Python Basics")

library.display_books()