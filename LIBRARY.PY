class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if isinstance(book, Book):
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print("Error: Item to borrow must be a valid Book object.")

    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"Error: '{title}' not currently borrowed by {self.name}.")

    def display_info(self):
        print(f"\nMember ID: {self.member_id}, Name: {self.name}")
        print("Borrowed Books:")
        if not self.borrowed_books:
            print("- None")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        print("--------------------")


print("Welcome to the Library System")
member_id = int(input("Enter Member ID: "))
name = input("Enter Member Name: ")
member = LibraryMember(member_id, name)

while True:
    print("\nChoose an action:")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. View Borrowed Books")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        book = Book(title, author)
        member.borrow_book(book)

    elif choice == "2":
        title = input("Enter the title of the book to return: ")
        member.return_book(title)

    elif choice == "3":
        member.display_info()

    elif choice == "4":
        print("Exiting the Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
