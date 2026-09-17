from student import Student


class Lecturer:
    def __init__(self, name, staff_id, password):
        self.name = name
        self.staff_id = staff_id
        self.password = password


lecturers = []
students = []


def create_lecturer_account():
    print("\n--- CREATE LECTURER ACCOUNT ---")

    name = input("Enter lecturer name: ")
    staff_id = input("Enter staff ID: ")
    password = input("Create password: ")

    # Check whether the staff ID already exists
    for lecturer in lecturers:
        if lecturer.staff_id == staff_id:
            print("An account with that staff ID already exists.")
            return

    new_lecturer = Lecturer(name, staff_id, password)
    lecturers.append(new_lecturer)

    print("Lecturer account created successfully.")


def login():
    print("\n--- LECTURER LOGIN ---")

    staff_id = input("Enter staff ID: ")
    password = input("Enter password: ")

    for lecturer in lecturers:
        if lecturer.staff_id == staff_id and lecturer.password == password:
            print("Login successful.")
            return lecturer

    print("Invalid staff ID or password.")
    return None


def register_student():
    print("\n--- REGISTER STUDENT ---")

    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")

    # Check whether the student already exists
    for student in students:
        if student.reg_no == reg_no:
            print("A student with that registration number already exists.")
            return

    new_student = Student(name, reg_no)
    students.append(new_student)

    print("Student registered successfully.")


def enter_mark():
    print("\n--- ENTER STUDENT MARK ---")

    reg_no = input("Enter student registration number: ")

    for student in students:
        if student.reg_no == reg_no:
            mark = float(input("Enter mark: "))
            student.add_mark(mark)
            return

    print("Student not found.")


def view_student_results():
    print("\n--- VIEW STUDENT RESULTS ---")

    reg_no = input("Enter student registration number: ")

    for student in students:
        if student.reg_no == reg_no:
            student.display_results()
            return

    print("Student not found.")


def list_students():
    print("\n--- REGISTERED STUDENTS ---")

    if len(students) == 0:
        print("No students have been registered.")
        return

    for student in students:
        print(student.name, "-", student.reg_no)


def lecturer_menu(current_lecturer):
    while True:
        print("\n================================")
        print("WELCOME,", current_lecturer.name)
        print("================================")
        print("1. Register Student")
        print("2. Enter Student Mark")
        print("3. View Student Results")
        print("4. List Students")
        print("5. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            enter_mark()

        elif choice == "3":
            view_student_results()

        elif choice == "4":
            list_students()

        elif choice == "5":
            print("Logged out successfully.")
            break

        else:
            print("Invalid option. Please try again.")


while True:
    print("\n================================")
    print("COURSEWORK MANAGEMENT SYSTEM")
    print("================================")
    print("1. Create Lecturer Account")
    print("2. Lecturer Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_lecturer_account()

    elif choice == "2":
        current_lecturer = login()

        if current_lecturer != None:
            lecturer_menu(current_lecturer)

    elif choice == "3":
        print("System closed.")
        break

    else:
        print("Invalid option. Please try again.")