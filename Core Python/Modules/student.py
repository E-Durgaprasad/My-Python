"""Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed."""

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
student1 =student("John",65)
student2 =student("hemanth",35)
if student1.is_passed():
    print(student1.name,"passed")
else:
    print("failed")
if student2.is_passed():
    print(student2.name,"passed")
else:
    print(student2.name,"failed")