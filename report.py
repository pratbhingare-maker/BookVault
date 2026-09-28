from datetime import datetime
from file_handler import load_data

BOOK_FILE = "data/books.json"
STUDENT_FILE = "data/students.json"
TRANSACTION_FILE = "data/transactions.json"


class Report:

    @staticmethod
    def generate_report():

        books = load_data(BOOK_FILE)
        students = load_data(STUDENT_FILE)
        transactions = load_data(TRANSACTION_FILE)

        total_book_copies = sum(
            book["quantity"] for book in books
        )

        available_book_copies = sum(
            book["available"] for book in books
        )

        issued_book_copies = (
            total_book_copies - available_book_copies
        )

        active_borrowings = sum(
            1
            for transaction in transactions
            if transaction["status"] == "Issued"
        )

        overdue_books = 0

        for transaction in transactions:

            if transaction["status"] == "Issued":

                due_date = datetime.strptime(
                    transaction["due_date"],
                    "%Y-%m-%d"
                ).date()

                if datetime.now().date() > due_date:
                    overdue_books += 1

        total_fine = sum(
            transaction["fine"]
            for transaction in transactions
        )

        print("\n========================================")
        print("          LIBRARY REPORT")
        print("========================================")
        print(f"Total Book Copies    : {total_book_copies}")
        print(f"Available Book Copies: {available_book_copies}")
        print(f"Issued Book Copies   : {issued_book_copies}")
        print(f"Total Students       : {len(students)}")
        print(f"Active Borrowings    : {active_borrowings}")
        print(f"Overdue Books        : {overdue_books}")
        print(f"Total Recorded Fine  : ₹{total_fine}")
        print("========================================")