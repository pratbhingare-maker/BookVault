from file_handler import load_data, save_data
from validation import validate_non_empty, validate_positive_number


BOOK_FILE = "data/books.json"


class Book:
    def __init__(self, book_id, title, author, category, quantity, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity
        self.available = available

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "quantity": self.quantity,
            "available": self.available
        }


def add_book():
    books = load_data(BOOK_FILE)

    try:
        book_id = validate_non_empty(
            input("Enter Book ID: "),
            "Book ID"
        )

        for book in books:
            if book["id"] == book_id:
                print("Book ID already exists.")
                return

        title = validate_non_empty(input("Enter Title: "), "Title")
        author = validate_non_empty(input("Enter Author: "), "Author")
        category = validate_non_empty(input("Enter Category: "), "Category")

        quantity = validate_positive_number(
            input("Enter Quantity: "),
            "Quantity"
        )

        book = Book(
            book_id,
            title,
            author,
            category,
            quantity,
            quantity
        )

        books.append(book.to_dict())
        save_data(BOOK_FILE, books)

        print("Book added successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def display_books():
    books = load_data(BOOK_FILE)

    if not books:
        print("No books found.")
        return

    print("\n========== BOOK LIST ==========")

    for book in books:
        print(f"Book ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Category: {book['category']}")
        print(f"Quantity: {book['quantity']}")
        print(f"Available: {book['available']}")
        print("------------------------------")


def search_book():
    books = load_data(BOOK_FILE)

    search = input("Enter Book ID or Title: ").strip().lower()

    found = False

    for book in books:
        if (
            search == book["id"].lower()
            or search in book["title"].lower()
        ):
            print("\nBook Found")
            print(f"Book ID: {book['id']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print(f"Quantity: {book['quantity']}")
            print(f"Available: {book['available']}")
            found = True

    if not found:
        print("Book not found.")


def update_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID to update: ").strip()

    for book in books:
        if book["id"] == book_id:

            try:
                title = validate_non_empty(
                    input("Enter New Title: "),
                    "Title"
                )

                author = validate_non_empty(
                    input("Enter New Author: "),
                    "Author"
                )

                category = validate_non_empty(
                    input("Enter New Category: "),
                    "Category"
                )

                new_quantity = validate_positive_number(
                    input("Enter New Quantity: "),
                    "Quantity"
                )

                issued_quantity = (
                    book["quantity"] - book["available"]
                )

                if new_quantity < issued_quantity:
                    print(
                        "Quantity cannot be less than currently issued copies."
                    )
                    return

                book["title"] = title
                book["author"] = author
                book["category"] = category
                book["quantity"] = new_quantity
                book["available"] = new_quantity - issued_quantity

                save_data(BOOK_FILE, books)

                print("Book updated successfully.")
                return

            except ValueError as error:
                print(f"Error: {error}")
                return

    print("Book not found.")


def remove_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID to remove: ").strip()

    for book in books:
        if book["id"] == book_id:

            issued_quantity = (
                book["quantity"] - book["available"]
            )

            if issued_quantity > 0:
                print("Cannot remove book while copies are issued.")
                return

            books.remove(book)
            save_data(BOOK_FILE, books)

            print("Book removed successfully.")
            return

    print("Book not found.")