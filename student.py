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