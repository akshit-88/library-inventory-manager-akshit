import json
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return [str(b) for b in self.books]

    def save_data(self):
        data = [b.to_dict() for b in self.books]
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            if self.file_path.exists():
                data = json.loads(self.file_path.read_text())
                self.books = [Book(**item) for item in data]
        except Exception:
            self.books = []  # corrupted file
