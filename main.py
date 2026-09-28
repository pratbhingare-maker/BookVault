from book import (
    add_book,
    display_books,
    search_book,
    update_book,
    remove_book
)

from student import (
    register_student,
    display_students,
    search_student
)

from transaction import (
    issue_book,
    return_book,
    transaction_history
)

from report import Report


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

        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            add_book()

        elif choice == "display":
            display_books()

        elif choice == "search":
            search_book()

        elif choice == "update":
            update_book()

        elif choice == "remove":
            remove_book()

        elif choice == "back":
            break

        else:
            print("Invalid choice. Please enter a valid command.")


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

        choice = input("Enter your choice: ").strip().lower()

        if choice == "register":
            register_student()

        elif choice == "display":
            display_students()

        elif choice == "search":
            search_student()

        elif choice == "back":
            break

        else:
            print("Invalid choice. Please enter a valid command.")


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

        choice = input("Enter your choice: ").strip().lower()

        if choice == "issue":
            issue_book()

        elif choice == "return":
            return_book()

        elif choice == "history":
            transaction_history()

        elif choice == "back":
            break

        else:
            print("Invalid choice. Please enter a valid command.")


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

        choice = input("Enter your choice: ").strip().lower()

        if choice == "book":
            book_menu()

        elif choice == "student":
            student_menu()

        elif choice in ["issue", "transaction"]:
            transaction_menu()

        elif choice == "report":
            Report.generate_report()

        elif choice == "exit":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid command.")


if __name__ == "__main__":
    main()