# library system.py with inheritance composition and margic methods
class Book:
    def __init__ (self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, Size: {self.file_size}MB"
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"Print Book: {self.title} by {self.author}, Pages: {self.pages_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)
       