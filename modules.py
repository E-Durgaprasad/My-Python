class Student:
    school_name="cvcorp"
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if self.marks>40:
            return "passed"
        return "failed"


stud1=Student("Julian",80)
stud2=Student("mon",35)
print(Student.school_name)
print(stud1.school_name)