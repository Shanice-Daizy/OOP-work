def calculate_average(self):
    if len(self.marks) == 0:
        return 0

    average = sum(self.marks) / len(self.marks)
    return average