class Student:
	def __init__(self, name, registration_number):
		self.name = name
		self.registration_number = registration_number
		self.marks = []

	def add_mark(self, mark):
		if 0 <= mark <= 100:
			self.marks.append(mark)
			print(mark, "has been added successfully.")
		else:
			print("Invalid mark. Mark must be between 0 and 100.")

	def calculate_average(self):
		if not self.marks:
			return 0

		return sum(self.marks) / len(self.marks)

	def get_grade(self):
		average = self.calculate_average()
		if average >= 70:
			return "A"
		if average >= 60:
			return "B"
		if average >= 50:
			return "C"
		if average >= 40:
			return "D"
		return "F"

	def has_passed(self):
		return self.calculate_average() >= 40

	def display_results(self):
		print("Name:", self.name)
		print("Registration number:", self.registration_number)
		print("Marks:", self.marks)
		print("Average:", self.calculate_average())
		print("Grade:", self.get_grade())
		print("Passed:", self.has_passed())