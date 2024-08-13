class Library:
    def __init__(self, name = ""):
        
        self.name = name
        self.books = []
        

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        if book in self.books:
            self.book.remove(book)
        else:
            print("book not found")


        
