class Book:
    def __init__(self,title):
        self.title = title
        self.available = True
class library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display(self):
        for book in self.books:
            print(book.title,book.available)

            False

b1 = Book('python')
b2 = Book('java')

lib = library()
lib.add_book(b1)
lib.add_book(b2)

lib.display()

lib.display()