"""
Zadanie 5: Klasa Library i Book
Stwórz klasy Library i Book.
Book powinna przechowywać tytuł, autora i status dostępności książki.
Library powinna przechowywać listę książek i mieć metody do dodawania książek oraz wyszukiwania książek po tytule.
"""

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)
            return f'Book {book} adding to the list.'
        else:
            return f'The book {book} is on the list.'

    def search_book(self, title):
        for book in self.book_list:
            if book.title == title:
                return 'The book is on the list'
            else:
                return 'The book is NOT on the list'


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

lib = Library()
book1 = Book("Python 101", "John Doe")
book2 = Book("Learning Python", "Jane Doe")
print(lib.add_book(book1))
print(lib.add_book(book2))
found_book = lib.search_book("Python 101")
print(found_book)

