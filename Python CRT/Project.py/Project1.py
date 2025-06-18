class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, {'Available' if self.available else 'Issued'})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' added successfully.")

    def issue_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        
        if not book:
            print("Book not found.")
            return
        if not member:
            print("Member not found.")
            return
        if not book.available:
            print("Book is already issued.")
            return
        
        book.available = False
        member.borrowed_books.append(book)
        print(f"Book '{book.title}' issued to {member.name}.")

    def return_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        
        if not book:
            print("Book not found.")
            return
        if not member:
            print("Member not found.")
            return
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned by {member.name}.")
        else:
            print(f"Book '{book.title}' was not issued to {member.name}.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                print(book)

    def view_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            print("\nLibrary Members:")
            for member in self.members:
                print(f"{member}, Borrowed: {[book.title for book in member.borrowed_books]}")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. View All Members")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        
        elif choice == '2':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)
        
        elif choice == '3':
            isbn = input("Enter ISBN of book to issue: ")
            member_id = input("Enter member ID: ")
            library.issue_book(isbn, member_id)
        
        elif choice == '4':
            isbn = input("Enter ISBN of book to return: ")
            member_id = input("Enter member ID: ")
            library.return_book(isbn, member_id)
        
        elif choice == '5':
            library.view_books()
        
        elif choice == '6':
            library.view_members()
        
        elif choice == '7':
            print("Exiting Library Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()