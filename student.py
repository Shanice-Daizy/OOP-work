#a student passes only if the average is 50 
#every individual mark they have has to be atleast 40

def has_passed(self):
    average = self.calculate_average()

    if average < 50:
        return False

    for mark in self.marks:
        if mark < 40:
            return False

    return True