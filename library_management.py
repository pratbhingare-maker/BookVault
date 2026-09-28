import json
from datetime import datetime, timedelta


# ============================================================
# CONFIGURATION
# ============================================================

BOOK_FILE = "books.json"
STUDENT_FILE = "students.json"
TRANSACTION_FILE = "transactions.json"

BORROW_DAYS = 7
FINE_PER_DAY = 5


# ============================================================
# FILE HANDLING
# ============================================================

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# ============================================================
# BOOK CLASS
# ============================================================

class Book:

    @staticmethod
    def add_book():

        print("\n========== ADD BOOK ==========")

        book_id = input("Enter Book ID: ").strip()

        books = load_data(BOOK_FILE)

        for book in books:
            if book["id"].lower() == book_id.lower():
                print("Book ID already exists.")
                return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author: ").strip()
        category = input("Enter Category: ").strip()

        while True:
            try:
                quantity = int(input("Enter Quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "category": category,
            "quantity": quantity,
            "available": quantity
        }

        books.append(new_book)

        save_data(BOOK_FILE, books)

        print("Book added successfully!")

    # --------------------------------------------------------

    @staticmethod
    def display_books():

        print("\n========== ALL BOOKS ==========")

        books = load_data(BOOK_FILE)

        if not books:
            print("No books found.")
            return

        for book in books:

            print("\nBook ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Category:", book["category"])
            print("Total Quantity:", book["quantity"])
            print("Available:", book["available"])

            print("-" * 35)

    # --------------------------------------------------------

    @staticmethod
    def search_book():

        print("\n========== SEARCH BOOK ==========")

        keyword = input("Enter Book ID or Title: ").strip().lower()

        books = load_data(BOOK_FILE)

        found = False

        for book in books:

            if (
                keyword in book["id"].lower()
                or keyword in book["title"].lower()
            ):

                print("\nBook ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Category:", book["category"])
                print("Available:", book["available"])

                found = True

        if not found:
            print("Book not found.")

    # --------------------------------------------------------

    @staticmethod
    def update_book():

        print("\n========== UPDATE BOOK ==========")

        book_id = input("Enter Book ID to update: ").strip()

        books = load_data(BOOK_FILE)

        for book in books:

            if book["id"].lower() == book_id.lower():

                print("Press Enter to keep the existing value.")

                title = input(
                    f"Title [{book['title']}]: "
                ).strip()

                author = input(
                    f"Author [{book['author']}]: "
                ).strip()

                category = input(
                    f"Category [{book['category']}]: "
                ).strip()

                if title:
                    book["title"] = title

                if author:
                    book["author"] = author

                if category:
                    book["category"] = category

                save_data(BOOK_FILE, books)

                print("Book updated successfully!")
                return

        print("Book not found.")

    # --------------------------------------------------------

    @staticmethod
    def remove_book():

        print("\n========== REMOVE BOOK ==========")

        book_id = input("Enter Book ID to remove: ").strip()

        books = load_data(BOOK_FILE)

        for book in books:

            if book["id"].lower() == book_id.lower():

                if book["available"] != book["quantity"]:
                    print(
                        "Cannot remove this book because "
                        "it is currently issued."
                    )
                    return

                books.remove(book)

                save_data(BOOK_FILE, books)

                print("Book removed successfully!")
                return

        print("Book not found.")


# ============================================================
# STUDENT CLASS
# ============================================================

class Student:

    @staticmethod
    def register_student():

        print("\n========== REGISTER STUDENT ==========")

        student_id = input("Enter Student ID: ").strip()

        students = load_data(STUDENT_FILE)

        for student in students:

            if student["id"].lower() == student_id.lower():

                print("Student ID already exists.")
                return

        name = input("Enter Student Name: ").strip()
        course = input("Enter Course: ").strip()
        email = input("Enter Email: ").strip()

        new_student = {
            "id": student_id,
            "name": name,
            "course": course,
            "email": email
        }

        students.append(new_student)

        save_data(STUDENT_FILE, students)

        print("Student registered successfully!")

    # --------------------------------------------------------

    @staticmethod
    def display_students():

        print("\n========== ALL STUDENTS ==========")

        students = load_data(STUDENT_FILE)

        if not students:
            print("No students found.")
            return

        for student in students:

            print("\nStudent ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Email:", student["email"])

            print("-" * 35)

    # --------------------------------------------------------

    @staticmethod
    def search_student():

        print("\n========== SEARCH STUDENT ==========")

        keyword = input(
            "Enter Student ID or Name: "
        ).strip().lower()

        students = load_data(STUDENT_FILE)

        found = False

        for student in students:

            if (
                keyword in student["id"].lower()
                or keyword in student["name"].lower()
            ):

                print("\nStudent ID:", student["id"])
                print("Name:", student["name"])
                print("Course:", student["course"])
                print("Email:", student["email"])

                found = True

        if not found:
            print("Student not found.")


# ============================================================
# TRANSACTION CLASS
# ============================================================

class Transaction:

    @staticmethod
    def issue_book():

        print("\n========== ISSUE BOOK ==========")

        student_id = input("Enter Student ID: ").strip()
        book_id = input("Enter Book ID: ").strip()

        students = load_data(STUDENT_FILE)
        books = load_data(BOOK_FILE)
        transactions = load_data(TRANSACTION_FILE)

        student_exists = False

        for student in students:

            if student["id"].lower() == student_id.lower():

                student_exists = True
                break

        if not student_exists:

            print("Student not found.")
            return

        selected_book = None

        for book in books:

            if book["id"].lower() == book_id.lower():

                selected_book = book
                break

        if selected_book is None:

            print("Book not found.")
            return

        if selected_book["available"] <= 0:

            print("Book is currently unavailable.")
            return

        for transaction in transactions:

            if (
                transaction["student_id"].lower() == student_id.lower()
                and transaction["book_id"].lower() == book_id.lower()
                and transaction["status"] == "Issued"
            ):

                print("This student already has this book.")
                return

        issue_date = datetime.now()

        due_date = issue_date + timedelta(
            days=BORROW_DAYS
        )

        transaction_id = len(transactions) + 1

        new_transaction = {

            "transaction_id": transaction_id,

            "student_id": student_id,

            "book_id": book_id,

            "issue_date":
                issue_date.strftime("%Y-%m-%d"),

            "due_date":
                due_date.strftime("%Y-%m-%d"),

            "return_date": "",

            "fine": 0,

            "status": "Issued"
        }

        transactions.append(new_transaction)

        selected_book["available"] -= 1

        save_data(BOOK_FILE, books)

        save_data(
            TRANSACTION_FILE,
            transactions
        )

        print("\nBook issued successfully!")

        print(
            "Issue Date:",
            issue_date.strftime("%Y-%m-%d")
        )

        print(
            "Due Date:",
            due_date.strftime("%Y-%m-%d")
        )

    # --------------------------------------------------------

    @staticmethod
    def return_book():

        print("\n========== RETURN BOOK ==========")

        student_id = input("Enter Student ID: ").strip()

        book_id = input("Enter Book ID: ").strip()

        books = load_data(BOOK_FILE)

        transactions = load_data(
            TRANSACTION_FILE
        )

        selected_transaction = None

        for transaction in transactions:

            if (
                transaction["student_id"].lower()
                == student_id.lower()

                and

                transaction["book_id"].lower()
                == book_id.lower()

                and

                transaction["status"] == "Issued"
            ):

                selected_transaction = transaction
                break

        if selected_transaction is None:

            print("No active transaction found.")
            return

        return_date = datetime.now()

        due_date = datetime.strptime(
            selected_transaction["due_date"],
            "%Y-%m-%d"
        )

        late_days = (
            return_date - due_date
        ).days

        if late_days < 0:
            late_days = 0

        fine = late_days * FINE_PER_DAY

        selected_transaction["return_date"] = (
            return_date.strftime("%Y-%m-%d")
        )

        selected_transaction["fine"] = fine

        selected_transaction["status"] = "Returned"

        for book in books:

            if book["id"].lower() == book_id.lower():

                book["available"] += 1
                break

        save_data(BOOK_FILE, books)

        save_data(
            TRANSACTION_FILE,
            transactions
        )

        print("\nBook returned successfully!")

        print(
            "Return Date:",
            return_date.strftime("%Y-%m-%d")
        )

        print("Late Days:", late_days)

        print("Fine: ₹", fine)

    # --------------------------------------------------------

    @staticmethod
    def transaction_history():

        print("\n========== TRANSACTION HISTORY ==========")

        transactions = load_data(
            TRANSACTION_FILE
        )

        if not transactions:

            print("No transactions found.")
            return

        for transaction in transactions:

            print(
                "\nTransaction ID:",
                transaction["transaction_id"]
            )

            print(
                "Student ID:",
                transaction["student_id"]
            )

            print(
                "Book ID:",
                transaction["book_id"]
            )

            print(
                "Issue Date:",
                transaction["issue_date"]
            )

            print(
                "Due Date:",
                transaction["due_date"]
            )

            print(
                "Return Date:",
                transaction["return_date"]
            )

            print(
                "Fine: ₹",
                transaction["fine"]
            )

            print(
                "Status:",
                transaction["status"]
            )

            print("-" * 40)


# ============================================================
# REPORT CLASS
# ============================================================

class Report:

    @staticmethod
    def generate_report():

        print("\n==========================================")
        print("             LIBRARY REPORT")
        print("==========================================")

        books = load_data(BOOK_FILE)

        students = load_data(
            STUDENT_FILE
        )

        transactions = load_data(
            TRANSACTION_FILE
        )

        total_books = sum(
            book["quantity"]
            for book in books
        )

        available_books = sum(
            book["available"]
            for book in books
        )

        issued_books = (
            total_books - available_books
        )

        active_borrowings = 0

        overdue_books = 0

        total_fine = 0

        today = datetime.now()

        for transaction in transactions:

            total_fine += transaction["fine"]

            if transaction["status"] == "Issued":

                active_borrowings += 1

                due_date = datetime.strptime(
                    transaction["due_date"],
                    "%Y-%m-%d"
                )

                if today > due_date:

                    overdue_books += 1

        print(
            "Total Book Copies:",
            total_books
        )

        print(
            "Available Book Copies:",
            available_books
        )

        print(
            "Issued Book Copies:",
            issued_books
        )

        print(
            "Total Students:",
            len(students)
        )

        print(
            "Active Borrowings:",
            active_borrowings
        )

        print(
            "Overdue Books:",
            overdue_books
        )

        print(
            "Total Recorded Fine: ₹",
            total_fine
        )

        print("==========================================")


# ============================================================
# BOOK MENU
# ============================================================

def book_menu():

    while True:

        print("\n================================")
        print("        BOOK MANAGEMENT")
        print("================================")

        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Remove Book")
        print("6. Back")

        print("================================")

        choice = input(
            "Enter your choice: "
        ).strip().lower()

        if choice == "add":
            Book.add_book()

        elif choice == "display":
            Book.display_books()

        elif choice == "search":
            Book.search_book()

        elif choice == "update":
            Book.update_book()

        elif choice == "remove":
            Book.remove_book()

        elif choice == "back":
            break

        else:

            print(
                "Invalid choice!"
                " Please enter the option name."
            )


# ============================================================
# STUDENT MENU
# ============================================================

def student_menu():

    while True:

        print("\n================================")
        print("       STUDENT MANAGEMENT")
        print("================================")

        print("1. Register Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Back")

        print("================================")

        choice = input(
            "Enter your choice: "
        ).strip().lower()

        if choice == "register":
            Student.register_student()

        elif choice == "display":
            Student.display_students()

        elif choice == "search":
            Student.search_student()

        elif choice == "back":
            break

        else:

            print(
                "Invalid choice!"
                " Please enter the option name."
            )


# ============================================================
# TRANSACTION MENU
# ============================================================

def transaction_menu():

    while True:

        print("\n================================")
        print("          TRANSACTIONS")
        print("================================")

        print("1. Issue Book")
        print("2. Return Book")
        print("3. Transaction History")
        print("4. Back")

        print("================================")

        choice = input(
            "Enter your choice: "
        ).strip().lower()

        if choice == "issue":
            Transaction.issue_book()

        elif choice == "return":
            Transaction.return_book()

        elif choice == "history":
            Transaction.transaction_history()

        elif choice == "back":
            break

        else:

            print(
                "Invalid choice!"
                " Please enter the option name."
            )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n============================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("============================================")

        print("1. Book Management")
        print("2. Student Management")
        print("3. Issue / Return Books")
        print("4. Library Report")
        print("5. Exit")

        print("============================================")

        choice = input(
            "Enter your choice: "
        ).strip().lower()

        if choice == "book":

            book_menu()

        elif choice == "student":

            student_menu()

        elif choice in ["issue", "transaction"]:

            transaction_menu()

        elif choice == "report":

            Report.generate_report()

        elif choice == "exit":

            print(
                "\nThank you for using "
                "Library Management System!"
            )

            break

        else:

            print(
                "Invalid choice!"
                " Please enter book, student, "
                "issue, report, or exit."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()