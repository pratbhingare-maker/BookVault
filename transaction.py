from datetime import datetime, timedelta

from file_handler import load_data, save_data


BOOK_FILE = "data/books.json"
STUDENT_FILE = "data/students.json"
TRANSACTION_FILE = "data/transactions.json"

BORROW_DAYS = 7
FINE_PER_DAY = 5


class Transaction:
    def __init__(
        self,
        transaction_id,
        student_id,
        book_id,
        issue_date,
        due_date,
        return_date=None,
        fine=0,
        status="Issued"
    ):
        self.transaction_id = transaction_id
        self.student_id = student_id
        self.book_id = book_id
        self.issue_date = issue_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine = fine
        self.status = status

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "student_id": self.student_id,
            "book_id": self.book_id,
            "issue_date": self.issue_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
            "fine": self.fine,
            "status": self.status
        }


def issue_book():
    books = load_data(BOOK_FILE)
    students = load_data(STUDENT_FILE)
    transactions = load_data(TRANSACTION_FILE)

    student_id = input("Enter Student ID: ").strip()
    book_id = input("Enter Book ID: ").strip()

    student_exists = any(
        student["id"] == student_id
        for student in students
    )

    if not student_exists:
        print("Student not found.")
        return

    book = None

    for item in books:
        if item["id"] == book_id:
            book = item
            break

    if book is None:
        print("Book not found.")
        return

    if book["available"] <= 0:
        print("Book is currently unavailable.")
        return

    for transaction in transactions:
        if (
            transaction["student_id"] == student_id
            and transaction["book_id"] == book_id
            and transaction["status"] == "Issued"
        ):
            print("This student already has this book.")
            return

    if transactions:
        transaction_id = max(
            transaction["transaction_id"]
            for transaction in transactions
        ) + 1
    else:
        transaction_id = 1

    issue_date = datetime.now().date()
    due_date = issue_date + timedelta(days=BORROW_DAYS)

    transaction = Transaction(
        transaction_id,
        student_id,
        book_id,
        str(issue_date),
        str(due_date)
    )

    transactions.append(transaction.to_dict())

    book["available"] -= 1

    save_data(BOOK_FILE, books)
    save_data(TRANSACTION_FILE, transactions)

    print("\nBook issued successfully.")
    print(f"Transaction ID: {transaction_id}")
    print(f"Issue Date: {issue_date}")
    print(f"Due Date: {due_date}")


def return_book():
    books = load_data(BOOK_FILE)
    transactions = load_data(TRANSACTION_FILE)

    student_id = input("Enter Student ID: ").strip()
    book_id = input("Enter Book ID: ").strip()

    transaction = None

    for item in transactions:
        if (
            item["student_id"] == student_id
            and item["book_id"] == book_id
            and item["status"] == "Issued"
        ):
            transaction = item
            break

    if transaction is None:
        print("No active transaction found.")
        return

    return_date = datetime.now().date()

    due_date = datetime.strptime(
        transaction["due_date"],
        "%Y-%m-%d"
    ).date()

    overdue_days = (return_date - due_date).days

    if overdue_days > 0:
        fine = overdue_days * FINE_PER_DAY
    else:
        fine = 0

    transaction["return_date"] = str(return_date)
    transaction["fine"] = fine
    transaction["status"] = "Returned"

    for book in books:
        if book["id"] == book_id:
            book["available"] += 1
            break

    save_data(BOOK_FILE, books)
    save_data(TRANSACTION_FILE, transactions)

    print("\nBook returned successfully.")
    print(f"Return Date: {return_date}")
    print(f"Fine: ₹{fine}")


def transaction_history():
    transactions = load_data(TRANSACTION_FILE)

    if not transactions:
        print("No transaction history found.")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    for transaction in transactions:
        print(f"Transaction ID: {transaction['transaction_id']}")
        print(f"Student ID: {transaction['student_id']}")
        print(f"Book ID: {transaction['book_id']}")
        print(f"Issue Date: {transaction['issue_date']}")
        print(f"Due Date: {transaction['due_date']}")
        print(f"Return Date: {transaction['return_date']}")
        print(f"Fine: ₹{transaction['fine']}")
        print(f"Status: {transaction['status']}")
        print("----------------------------------------")