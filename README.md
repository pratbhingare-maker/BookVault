# Library Management System

## Overview

The Library Management System is a Python-based terminal application designed to manage basic library operations in an organized and efficient way.

The system allows users to manage books and students, issue and return books, maintain transaction records, calculate fines, and generate library reports.

The project follows a modular structure where different responsibilities are separated into individual Python files.

## Features

### Book Management
- Add books
- Display books
- Search books
- Update book details
- Remove books
- Track total and available copies

### Student Management
- Register students
- Display students
- Search students
- Validate student information

### Issue and Return Management
- Issue books to registered students
- Return books
- Track issue and due dates
- Calculate overdue fines
- Prevent issuing unavailable books

### Transaction Management
- Generate unique transaction IDs
- Maintain transaction history
- Track issued and returned books
- Store transaction information persistently

### Library Reports
- Total book copies
- Available book copies
- Issued book copies
- Total students
- Active borrowings
- Overdue books
- Total recorded fines

## Technologies Used

- Python 3
- JSON
- Git
- GitHub
- Terminal / Command Prompt

**## Project Structure**

```text
project/
│
├── main.py
├── book.py
├── student.py
├── transaction.py
├── report.py
├── file_handler.py
├── validation.py
├── library_management.py
│
├── data/
│   ├── books.json
│   ├── students.json
│   └── transactions.json
│
├── docs/
│   ├── Diagram/
│   ├── Documentation/
│   └── Screenshot/
│
├── report/
│   ├── final_report.md
│   └── BUILDVAULT.pdf
│
├── statement.md
├── README.md
└── .gitignore