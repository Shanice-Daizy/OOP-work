class Student:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no
        self.marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks.append(mark)
            print(mark, "has been added successfully.")
        else:
            print("Invalid mark. Mark must be between 0 and 100.")

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        total = sum(self.marks)
        average = total / len(self.marks)

        return average

    # A student passes only if the average is at least 50 and
    # every individual mark is at least 40.
    def has_passed(self):
        average = self.calculate_average()

        if average < 50:
            return False

        for mark in self.marks:
            if mark < 40:
                return False

        return True
