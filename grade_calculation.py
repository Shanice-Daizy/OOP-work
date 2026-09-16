class Student:
    def _init_(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number
        self.marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks.append(mark)
        else:
            print("Invalid mark. Mark must be between 0 and 100.")

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()

        if average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"