# Testing and Results

## 1. Testing Approach

The Library Management System was tested manually using different valid and invalid inputs. Each major module and its important functions were tested to verify that the expected output was produced.

## 2. Book Management Testing

| Test Case | Input/Action | Expected Result | Result |
|---|---|---|---|
| Add Book | Enter valid book details | Book is added successfully | Passed |
| Display Books | Select display option | All stored books are displayed | Passed |
| Search Book | Enter Book ID or title | Matching book is displayed | Passed |
| Update Book | Enter valid updated details | Book information is updated | Passed |
| Remove Book | Remove an available book | Book is removed successfully | Passed |

## 3. Student Management Testing

| Test Case | Input/Action | Expected Result | Result |
|---|---|---|---|
| Register Student | Enter valid student details | Student is registered successfully | Passed |
| Display Students | Select display option | Registered students are displayed | Passed |
| Search Student | Enter Student ID or name | Matching student is displayed | Passed |
| Duplicate Student ID | Enter an existing Student ID | Duplicate registration is prevented | Passed |

## 4. Transaction Testing

| Test Case | Input/Action | Expected Result | Result |
|---|---|---|---|
| Issue Book | Enter valid Student ID and Book ID | Book is issued successfully | Passed |
| Issue Unavailable Book | Select a book with no available copies | Issue operation is prevented | Passed |
| Duplicate Issue | Issue the same book to the same student again | Duplicate issue is prevented | Passed |
| Return Book | Return an issued book | Book availability is increased | Passed |
| Fine Calculation | Return an overdue book | Fine is calculated correctly | Passed |
| Transaction History | Select history option | Previous transactions are displayed | Passed |

## 5. Report Testing

| Test Case | Input/Action | Expected Result | Result |
|---|---|---|---|
| Generate Report | Select report option | Library statistics are displayed | Passed |

The report successfully displayed total book copies, available copies, issued copies, total students, active borrowings, overdue books, and recorded fines.

## 6. Validation Testing

The system was tested with invalid inputs such as empty fields, invalid quantities, duplicate IDs, and invalid email addresses.

The system displayed appropriate error messages and prevented invalid data from being stored.

## 7. Data Persistence Testing

The program was closed and executed again after storing records.

Previously saved book, student, and transaction data remained available because the information was stored in JSON files.

## 8. Final Testing Result

All major functional modules were tested successfully.

The tested modules include:

- Book Management
- Student Management
- Transaction Management
- Library Report
- Input Validation
- JSON Data Storage
- Menu Navigation

The system successfully completed the required library management operations during testing.