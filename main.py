class Student:
    def __init__(self, name, registration_number):
        self.name = name
        self.registration_number = registration_number
        self.marks = []

    def add_mark(self, mark):
        # Only accept marks between 0 and 100
        if mark >= 0 and mark <= 100:
            self.marks.append(mark)
            print(mark, "has been added successfully.")
        else:
            print("Invalid mark. Mark must be between 0 and 100.")

    def calculate_average(self):
        # Avoid division by zero if no marks have been added
        if len(self.marks) == 0:
            return 0

        total = sum(self.marks)
        average = total / len(self.marks)

        return average


# Testing the Student class
student1 = Student("Carl", "S23B23/001")

student1.add_mark(75)
student1.add_mark(80)
student1.add_mark(65)

print("Marks:", student1.marks)
print("Average:", student1.calculate_average())