import json


BOOK_FILE = "data/books.json"
STUDENT_FILE = "data/students.json"
TRANSACTION_FILE = "data/transactions.json"


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)