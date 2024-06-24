"""
Zadanie : System Biblioteczny
Napisz klasy dla systemu bibliotecznego. 
Stwórz klasę Ksiazka, która będzie miała atrybuty jak tytul, autor, rok_wydania, oraz dostepnosc.
Dodaj klasę Biblioteka, która będzie zarządzać kolekcją książek i umożliwiać wypożyczanie oraz zwracanie książek.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.avalible = True

    def rent_book(self):
        self.avalible = False

    def return_book(self):
        self.avalible = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)
            return f'Added {book} to the list.'

    def remove_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            return f'Remove {book} to the list.'
        else:
            return f'{book} if not on the list.'

    def display_avalible_book(self):
        avalible_title = [book.title for book in self.book_list if book.avalible]
        if avalible_title:
            return avalible_title
        else:
            return 'No avalible books.'

    def rent_book(self, title):
        for book in self.book_list:
            if book.title == title:
                if book.avalible:
                    book.avalible = False
                    return f'Rented {title}.'
                else:
                    return f'{title} is rent.'
        return f'No {title} on the list.'

    def return_book(self, title):
        for book in self.book_list:
            if book.title == title:
                if not book.avalible:
                    book.avalible = True
                    return f'Returned {title}.'
                else:
                    return f'{title} is avalible.'
        return f'No {title} on the list.'



book1 = Book("Wiedźmin", "Andrzej Sapkowski", 1993)
book2 = Book("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997)
book3 = Book("1984", "George Orwell", 1949)

library = Library()

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

# Wypożyczenie książki
print(library.rent_book("Wiedźmin"))  # Wypożyczono Wiedźmin.

# Sprawdzenie dostępnych książek
print(library.display_avalible_book())

# Wypożyczenie już wypożyczonej książki
print(library.rent_book("Wiedźmin"))  # Wiedźmin jest już wypożyczona.

# Zwrot książki
print(library.return_book("Wiedźmin"))  # Zwrócono Wiedźmin.

# Sprawdzenie dostępnych książek po zwrocie
print(library.display_avalible_book())


# Próba wypożyczenia książki, która nie istnieje w bibliotece
print(library.rent_book("Hobbit"))  # Książka o tytule Hobbit nie jest dostępna w bibliotece.

# Usunięcie książki z biblioteki
print(library.remove_book(book2))  # Usunięto Harry Potter i Kamień Filozoficzny by J.K. Rowling (1997) z listy.

# Sprawdzenie dostępnych książek po usunięciu
print(library.display_avalible_book())



