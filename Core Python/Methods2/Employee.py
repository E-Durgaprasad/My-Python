"""""Q3. Create an Employee class that:
*Keeps a minimum experience required for promotion (shared across all employees).
*Stores employee name, experience, and department.
*Has a method to check eligibility for promotion.
*Provides a function to update promotion criteria globally.
*Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
1.Creating employees from different departments.
2.Changing promotion criteria.
3.Displaying eligibility results and department validation."""""

class Employee:
    minimum_experience=1
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def promotion(self):
        if self.experience>=Employee.minimum_experience:
            return "you are Eligible"
        else:
            return "you are notEligible"
    @classmethod
    def change_experience(cls,new_experience):
        cls.minimum_experience=new_experience
    @staticmethod
    def validation(department):
        if department in ["HR", "Tech", "Admin"]:
            return "valid Department"
        else:
            return "Invalid Department"
emp=Employee(name="sanju",experience=2,department="HR")
emp1=Employee(name="raj",experience=1,department="Admin")
emp2=Employee(name="kon",experience=0,department="lecture")
print(emp.promotion())
print(emp.promotion())
print(emp1.promotion())
Employee.change_experience(2)
print(emp1.promotion())
print(emp.validation("HR"))

print("\n Department Validation")

print(emp.validation("HR"))
print(Employee.validation("Finance"))








