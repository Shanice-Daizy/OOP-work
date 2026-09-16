def add_mark(self, mark):
    if mark >= 0 and mark <= 100:
        self.marks.append(mark)
        print(mark, "has been added successfully.")
    else:
        print("Invalid mark. Mark must be between 0 and 100.")