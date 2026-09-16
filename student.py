def get_grade(self):#defines the get_grade method for the student instance
    average = self.calculate_average()#calculates the average

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
        #determines the grade based on average
