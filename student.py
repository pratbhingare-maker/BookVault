from file_handler import load_data, save_data
from validation import validate_non_empty, validate_email


STUDENT_FILE = "data/students.json"


class Student:
    def __init__(self, student_id, name, course, email):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.email = email

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "course": self.course,
            "email": self.email
        }


def register_student():
    students = load_data(STUDENT_FILE)

    try:
        student_id = validate_non_empty(
            input("Enter Student ID: "),
            "Student ID"
        )

        for student in students:
            if student["id"] == student_id:
                print("Student ID already exists.")
                return

        name = validate_non_empty(
            input("Enter Student Name: "),
            "Student Name"
        )

        course = validate_non_empty(
            input("Enter Course: "),
            "Course"
        )

        email = validate_email(
            input("Enter Email: ")
        )

        student = Student(
            student_id,
            name,
            course,
            email
        )

        students.append(student.to_dict())
        save_data(STUDENT_FILE, students)

        print("Student registered successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def display_students():
    students = load_data(STUDENT_FILE)

    if not students:
        print("No students found.")
        return

    print("\n========== STUDENT LIST ==========")

    for student in students:
        print(f"Student ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Email: {student['email']}")
        print("------------------------------")


def search_student():
    students = load_data(STUDENT_FILE)

    search = input("Enter Student ID or Name: ").strip().lower()

    found = False

    for student in students:
        if (
            search == student["id"].lower()
            or search in student["name"].lower()
        ):
            print("\nStudent Found")
            print(f"Student ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Email: {student['email']}")
            found = True

    if not found:
        print("Student not found.")