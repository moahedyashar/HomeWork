class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
    
    def get_title(self):
        return self._title
    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author
    def set_author(self, author):
        self._author = author

    def get_pages(self):
        return self._pages
    def set_pages(self, pages):
        self._pages = pages

book = Book("masnawi", "mawlana", 500)

book.set_title("manawy")
print(book.get_title())

