# Design Decisions and Rationale

## 1. Modular Program Structure

The project is divided into separate Python modules such as `book.py`, `student.py`, `transaction.py`, `report.py`, `validation.py`, and `file_handler.py`.

### Rationale

A modular structure makes the program easier to understand, test, maintain, and modify. Each module is responsible for a specific part of the library system.

---

## 2. Use of Object-Oriented Programming

Classes such as `Book`, `Student`, `Transaction`, and `Report` are used in the project.

### Rationale

Object-oriented programming helps represent real-world entities such as books, students, and library transactions. It also improves code organization and reusability.

---

## 3. JSON-Based Data Storage

The system stores data in three JSON files:

- `books.json`
- `students.json`
- `transactions.json`

### Rationale

JSON provides a simple and readable way to store structured data without requiring a database system. It also allows the data to remain available after the program is closed.

---

## 4. Separate File Handling Module

The `file_handler.py` module contains common functions for loading and saving JSON data.

### Rationale

Keeping file operations in a separate module avoids repeating the same code in multiple modules and improves maintainability.

---

## 5. Input Validation

The `validation.py` module contains functions for checking user input.

### Rationale

Validation prevents invalid data such as empty fields, non-positive quantities, and invalid email addresses from being stored in the system.

---

## 6. Transaction-Based Book Issue and Return

Book issuing and returning are handled through the `transaction.py` module.

### Rationale

Transactions connect students and books and allow the system to maintain issue dates, due dates, return dates, fines, and transaction history.

---

## 7. Fine Calculation

A borrowing period of 7 days is used, with a fine of ₹5 per overdue day.

### Rationale

This provides a simple mechanism for demonstrating date handling and overdue fine calculation in the project.

---

## 8. Menu-Based Interface

The system uses a command-based menu where the available options are displayed using numbers, while the user enters commands such as `book`, `student`, `issue`, `report`, and `exit`.

### Rationale

This approach keeps the interface simple and easy to operate in a terminal environment while demonstrating Python input, conditions, loops, and functions.

---

## 9. Separate Report Module

The `report.py` module generates a summary of the library.

### Rationale

Separating reporting functionality keeps the main program organized and allows library statistics to be calculated independently.

---

## 10. Future Database Migration

The current system uses JSON files, but the storage layer can be replaced with a database in a future version.

### Rationale

Separating file-handling logic from the main modules makes it easier to upgrade the storage system without redesigning the entire application.