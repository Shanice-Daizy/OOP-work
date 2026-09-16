from student import Student


# Testing the Student class
student1 = Student("Carl", "S23B23/001")

student1.add_mark(75)
student1.add_mark(80)
student1.add_mark(65)

print("Marks:", student1.marks)
print("Average:", student1.calculate_average())
