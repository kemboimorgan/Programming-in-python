class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def display_info(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(book.title, "by", book.author)

b1 = Book("1984", "George Orwell")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
m1 = LibraryMember(1, "Morgan")
m1.borrow_book(b1)
m1.borrow_book(b2)
m1.display_info()
m1.return_book(b1)
m1.display_info()

