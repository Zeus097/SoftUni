class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self, title):
        try:
            book = [book for book in self.books if book.title == title][0]
            return book.title
        except IndexError:
            return "Sorry, book not found."

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)


library = Library()
for num in range(1, 6):
    b = Book(f"Title: {num}", f"Author: {num}")
    library.add_book(b)

# Testing:
print(library.get_books("asd"))
print(library.get_books("Title: 1"))

