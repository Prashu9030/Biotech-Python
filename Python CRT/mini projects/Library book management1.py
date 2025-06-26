class Library:
    def __init__(self):
        self.books = {
            "Python Programming": 3,
            "Data Structures": 2,
            "Machine Learning": 1,
            "Algorithms": 4
        }

    def display_books(self):
        print("\nAvailable Books:")
        for book, count in self.books.items():
            print(f"{book} - {count} copies")

    def add_book(self, book_name, quantity):
        if book_name in self.books:
            self.books[book_name] += quantity
        else:
            self.books[book_name] = quantity
        print(f"\n{quantity} copies of '{book_name}' added to the library.")

    def borrow_book(self, book_name):
        if self.books.get(book_name, 0) > 0:
            self.books[book_name] -= 1
            print(f"\nYou have borrowed '{book_name}'. Please return it on time.")
        else:
            print(f"\nSorry! '{book_name}' is not available right now.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1
        print(f"\nThank you for returning '{book_name}'.")


def main():
    lib = Library()

    while True:
        print("\n==== Library Menu ====")
        print("1. Display available books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            lib.display_books()
        elif choice == "2":
            book = input("Enter book name to add: ")
            qty = int(input("Enter number of copies: "))
            lib.add_book(book, qty)
        elif choice == "3":
            book = input("Enter book name to borrow: ")
            lib.borrow_book(book)
        elif choice == "4":
            book = input("Enter book name to return: ")
            lib.return_book(book)
        elif choice == "5":
            print("\nThank you for using the Library Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
