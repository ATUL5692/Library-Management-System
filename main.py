# Library Management System

# Initialize library as empty lists
library_books = []  # List of available books
issued_books = []   # List of issued books

# Function to add a book to the library
def add_book(book_name):
    library_books.append(book_name)
    print(f"'{book_name}' has been added to the library.\n")

# Function to issue a book
def issue_book(book_name):
    if book_name in library_books:
        library_books.remove(book_name)
        issued_books.append(book_name)
        print(f"'{book_name}' has been issued.\n")
    else:
        print(f"'{book_name}' is not available in the library.\n")

# Function to return a book
def return_book(book_name):
    if book_name in issued_books:
        issued_books.remove(book_name)
        library_books.append(book_name)
        print(f"'{book_name}' has been returned to the library.\n")
    else:
        print(f"'{book_name}' was not issued.\n")

# Function to view all books in the library
def view_books():
    print("\nAvailable Books in the Library:")
    if not library_books:
        print("No books are available.")
    else:
        for book in library_books:
            print(f"- {book}")

    print("\nIssued Books:")
    if not issued_books:
        print("No books have been issued.")
    else:
        for book in issued_books:
            print(f"- {book}")
    print("\n")

# Menu system to interact with the library system
def library_menu():
    while True:
        print("Library Menu")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        # Take user input
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            add_book(book_name)
        elif choice == '2':
            book_name = input("Enter the name of the book to issue: ")
            issue_book(book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book to return: ")
            return_book(book_name)
        elif choice == '4':
            view_books()
        elif choice == '5':
            print("Exiting the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

# Start the Library Management System
library_menu()
