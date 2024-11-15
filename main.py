import mysql.connector
import datetime

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",        # Database host
    user="root",             # Database username
    password="M@ngo112",     # Database password
    database="library"       # Database name
)

# Create a cursor object to interact with the database
cursor = mydb.cursor()

def add_book():
    print("Please provide the following details :)")
    num = int(input("How many books do you want to add? "))
    for i in range(num):
        book_name = input("Enter book name: ")
        mrp = float(input("Enter M.R.P of the book: "))
        writer = input("Who is the writer of the book: ")
        print("Thank you for the information")
        try:
            sql = "INSERT INTO Books (book_name, mrp, writer) VALUES (%s, %s, %s)"
            values = (book_name, mrp, writer)
            cursor.execute(sql, values)
            mydb.commit()
            print("Book added successfully in the library.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


def return_book():
    try:
        R_book_name = input("Enter the name of the book to return: ")
        Book_condition = input("Enter a Book Condition:")


        # Fetch the issued book details
        cursor.execute("SELECT issue_id, book_id, due_date FROM IssuedBooks WHERE book_name = %s", (R_book_name,))
        book = cursor.fetchone()

        if book:
            issue_id = book[0]
            book_id = book[1]
            due_date = book[2]

            # Calculate penalty if the return is overdue
            return_date = datetime.date.today()
            if return_date > due_date:
                days_late = (return_date - due_date).days
                penalty = days_late * 5  # Assume 5 is the penalty per day
            else:
                penalty = 0

            if Book_condition.upper() == "GOOD":
                penalty = penalty + 0
            else:
                print("Your Book Condition is Bad you have to Pay Rs.100")
                penalty = penalty + 100

            # Insert return details into ReturnedBooks table
            cursor.execute("""
                INSERT INTO ReturnedBooks (issue_id, book_id, return_date, penalty, book_condition)
                VALUES (%s, %s, %s, %s ,%s)
            """, (issue_id, book_id, return_date, penalty,Book_condition.upper()))
            mydb.commit()

            print(f"Book '{R_book_name}' has been returned successfully.")
            print(f"Return Date: {return_date}, Penalty: {penalty}")
        else:
            print(f"Book '{R_book_name}' is not issued.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def Issue_book():
    print("Please provide the following details before issuing books.")
    I_book = input("Please give me the name of the book: ")
    try:
        cursor.execute("SELECT book_name, book_id FROM Books WHERE book_name = %s", (I_book,))
        book = cursor.fetchone()

        if book:
            book_name = book[0]  # Extract book name
            book_id = book[1]  # Extract book ID

            # Issue the book by inserting into IssuedBooks table
            issued_date = datetime.date.today()
            due_date = issued_date + datetime.timedelta(days=14)

            cursor.execute("INSERT INTO IssuedBooks (book_id, book_name, issued_date, due_date) VALUES (%s, %s, %s, %s)",
                           (book_id, book_name, issued_date, due_date))
            mydb.commit()  # Commit the changes to the database

            print(f"Book '{book_name}' has been issued successfully.")
            print(f"Issued Date: {issued_date}, Due Date: {due_date}")
        else:
            print(f"Book '{I_book}' not found in the library.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        mydb.close()

def view_books():
    # Placeholder function to view books
    print("Displaying all available books...")

def library_menu():
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        # Take user input
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            Issue_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            fetch_all_books()
        elif choice == '5':
            print("Thanking-You for visiting our Library \n Have a Nice Day...")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

# Function to fetch and display all rows from the Books table
def fetch_all_books():
    try:
        # Execute the SELECT query to retrieve all rows
        cursor.execute("SELECT * FROM Books")

        # Fetch all the results
        rows = cursor.fetchall()

        # Check if there are rows in the result set
        if rows:
            print("Books in the library:")
            print("------------------------------")
            for row in rows:
                print("Name of  the Book:",row[1])
                print("Price of the  Book:",row[2])
                print("Writer of the Book:",row[3])
                print("                   ")
        else:
            print("No books found in the library.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Start the Library Management System
library_menu()

# Close the cursor and the connection once the program ends
cursor.close()
mydb.close()
