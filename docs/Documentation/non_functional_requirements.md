# Non-Functional Requirements

## 1. Usability

- The system shall provide a simple menu-based interface.
- Menu options shall be clearly displayed with numbers.
- Users shall enter commands using simple words.
- The system shall display clear success and error messages.

## 2. Reliability

- The system shall preserve data after the program is closed.
- Book, student, and transaction records shall be stored in JSON files.
- The system shall prevent invalid transactions such as issuing unavailable books.
- The system shall maintain consistent book availability after issue and return operations.

## 3. Performance

- The system shall load and save records efficiently.
- Search operations shall provide results without unnecessary processing.
- The system shall support multiple book, student, and transaction records.

## 4. Maintainability

- The system shall be divided into separate Python modules.
- Each module shall perform a specific responsibility.
- Common functions such as file handling and validation shall be reused.
- The code shall use meaningful variable, function, and class names.

## 5. Error Handling

- The system shall handle missing data files.
- Invalid quantities shall be rejected.
- Empty required fields shall be rejected.
- Duplicate Book IDs and Student IDs shall be prevented.
- Invalid email addresses shall display an appropriate error message.

## 6. Data Integrity

- Book availability shall be updated whenever a book is issued or returned.
- A book shall not be issued when no copies are available.
- A student shall not receive the same book while it is already issued.
- Books with currently issued copies shall not be removed.

## 7. Scalability

- The modular structure shall allow additional features to be added later.
- The JSON storage approach can be replaced with a database in future versions.
- Additional modules such as authentication, notifications, or fine payment can be integrated later.