"""Q1. Create a class Student that:
*Keeps track of the total number of students created.
*Determines whether a student passed or failed based on a shared passing mark.
*Provides a method to curve marks by increasing everyone’s marks by a percentage.
*Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
Demonstrate:
1.Creating multiple students.
2.Applying a grading curve.
3.Displaying updated results with letter grades.
"""

class students:
    total_students=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        students.total_students+=1
    def is_passed(self):
        if self.marks<=35:
            return "Failed"
        else:
            return "Passed"

    def curve_marks(self):
        self.marks=self.marks+5
        return self.marks

    def Grade(self):
        if (self.marks>80) and (self.marks<100):
            return "0"
        elif (self.marks>60) and (self.marks<80):
            return "A"
        elif (self.marks>40) and (self.marks<60):
            return "B"
        elif (self.marks>35):
            return "C"
        elif (self.marks<35):
            return "F"


std=students('ram',36)
std1=students('sham',20)
print(students.total_students)
print(std.is_passed())
print(std1.is_passed())
print(std.Grade())
print(std1.Grade())
print(std.curve_marks())


