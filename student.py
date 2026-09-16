


    def display_results(self):
        print("Name:", self.name)
        print("Registration Number:", self.registration_number)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())
        print("Grade:", self.get_grade())

        if self.has_passed():
            print("Status: PASSED")
        else:
            print("Status: FAILED")


# DEMONSTRATION

student1 = Student("Alex", "S24B23/001")

student1.add_mark(80)
student1.add_mark(75)
student1.add_mark(65)


student2 = Student("Mary", "S24B23/002")

student2.add_mark(90)
student2.add_mark(70)
student2.add_mark(35)

# Invalid action - this mark must be refused
student2.add_mark(120)


print("\nSTUDENT 1 RESULTS")
student1.display_results()

print("\nSTUDENT 2 RESULTS")
student2.display_results() 
    
    
    
    
    
    
    
    
    
    